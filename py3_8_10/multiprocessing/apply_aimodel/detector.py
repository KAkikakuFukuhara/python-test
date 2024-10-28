from __future__ import division
import os
import cv2
import numpy as np
import pickle
import time
import pprint
from keras_frcnn import config
from keras_frcnn.config import Config
import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from keras_frcnn import roi_helpers
import argparse
import keras_frcnn.resnet as nn
from keras_frcnn.visualize import draw_boxes_and_label_on_image_cv2
from utils.process import *
import copy


class FasterRCNNDetector(object):

    def __init__(self, model_path):
        if os.path.exists('config.pickle'):
            with open('config.pickle', 'rb') as f:
                self.cfg = pickle.load(f)
        else:
            self.cfg = Config()
            print('Not found previous train and saved config.pickle file. may lose class map info.')
        self.model_path = model_path
        self._init_model()


    def _init_model(self):
        self.cfg.use_horizontal_flips = False
        self.cfg.use_vertical_flips = False
        self.cfg.rot_90 = False
        self.cfg.model_path = f"./{self.model_path}"

        class_mapping = self.cfg.class_mapping
        if 'bg' not in class_mapping:
            class_mapping['bg'] = len(class_mapping)

        self.class_mapping = {v: k for k, v in class_mapping.items()}
        input_shape_img = (None, None, 3)
        input_shape_features = (None, None, 1024)

        img_input = Input(shape=input_shape_img)
        roi_input = Input(shape=(self.cfg.num_rois, 4))
        feature_map_input = Input(shape=input_shape_features)

        shared_layers = nn.nn_base(img_input, trainable=False)

        num_anchors = len(self.cfg.anchor_box_scales) * len(self.cfg.anchor_box_ratios)
        rpn_layers = nn.rpn(shared_layers, num_anchors)
        classifier = nn.classifier(feature_map_input, roi_input, self.cfg.num_rois, nb_classes=len(class_mapping), trainable=True)

        self.model_rpn = Model(img_input, rpn_layers)
        model_classifier_only = Model([feature_map_input, roi_input], classifier)
        
        self.model_classifier = Model([feature_map_input, roi_input], classifier)

        model_path = self.cfg.model_path
        print('Loading weights from {}'.format(model_path))
        if not os.path.exists(model_path):
            model_path = self.cfg.model_path
            print('previous model path not found or not exist, using specific one: ', self.cfg.model_path)
        self.model_rpn.load_weights(model_path, by_name=True)
        self.model_classifier.load_weights(model_path, by_name=True)

        self.model_rpn.compile(optimizer='sgd', loss='mse')
        self.model_classifier.compile(optimizer='sgd', loss='mse')


    def format_img_size(img, cfg):
        img_min_side = float(cfg.im_size)
        (height, width, _) = img.shape

        if width <= height:
            ratio = img_min_side / width
            new_height = int(ratio * height)
            new_width = int(img_min_side)
        else:
            ratio = img_min_side / height
            new_width = int(ratio * width)
            new_height = int(img_min_side)
        img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
        return img, ratio


    def format_img_channels(img, cfg):
        #img = img[:, :, (2, 1, 0)]
        img = img.astype(np.float32)
        img[:, :, 0] -= cfg.img_channel_mean[0]
        img[:, :, 1] -= cfg.img_channel_mean[1]
        img[:, :, 2] -= cfg.img_channel_mean[2]
        img /= cfg.img_scaling_factor
        img = np.transpose(img, (2, 0, 1))
        img = np.expand_dims(img, axis=0)
        return img


    def format_img(img, C):
        img, ratio = format_img_size(img, C)
        img = format_img_channels(img, C)
        return img, ratio


    def get_real_coordinates(ratio, x1, y1, x2, y2):
        real_x1 = int(round(x1 // ratio))
        real_y1 = int(round(y1 // ratio))
        real_x2 = int(round(x2 // ratio))
        real_y2 = int(round(y2 // ratio))
        
        return real_x1, real_y1, real_x2, real_y2

    def detect_on_image(self, img):
        tic = time.time()

        X, ratio = format_img(img, self.cfg)
        X = np.transpose(X, (0, 2, 3, 1))
        [Y1, Y2, F] = self.model_rpn.predict(X)

        result = roi_helpers.rpn_to_roi(Y1, Y2, self.cfg, overlap_thresh=0.7)

        result[:, 2] -= result[:, 0]
        result[:, 3] -= result[:, 1]
        bbox_threshold = 0.8

        dict_list = []
        one_time_dict = {"label":"",
                         "score":"",
                         "bbox":""}

        boxes = dict()
        for jk in range(result.shape[0] // self.cfg.num_rois + 1):
            rois = np.expand_dims(result[self.cfg.num_rois * jk:self.cfg.num_rois * (jk + 1), :], axis=0)

            if rois.shape[1] == 0:
                break
            if jk == result.shape[0] // self.cfg.num_rois:
                curr_shape = rois.shape
                target_shape = (curr_shape[0], self.cfg.num_rois, curr_shape[2])
                rois_padded = np.zeros(target_shape).astype(rois.dtype)
                rois_padded[:, :curr_shape[1], :] = rois
                rois_padded[0, curr_shape[1]:, :] = rois[0, 0, :]
                rois = rois_padded

            [p_cls, p_regr] = self.model_classifier.predict([F, rois])

            for ii in range(p_cls.shape[1]):
                if np.max(p_cls[0, ii, :]) < bbox_threshold or np.argmax(p_cls[0, ii, :]) == (p_cls.shape[2] - 1):
                    continue

                cls_num = np.argmax(p_cls[0, ii, :])
                if cls_num not in boxes.keys():
                    boxes[cls_num] = []
                (x, y, w, h) = rois[0, ii, :]
                try:
                    (tx, ty, tw, th) = p_regr[0, ii, 4 * cls_num:4 * (cls_num + 1)]
                    tx /= self.cfg.classifier_regr_std[0]
                    ty /= self.cfg.classifier_regr_std[1]
                    tw /= self.cfg.classifier_regr_std[2]
                    th /= self.cfg.classifier_regr_std[3]
                    x, y, w, h = roi_helpers.apply_regr(x, y, w, h, tx, ty, tw, th)
                except Exception as e:
                    print(e)
                    pass
                boxes[cls_num].append(
                    [self.cfg.rpn_stride * x, self.cfg.rpn_stride * y, self.cfg.rpn_stride * (x + w), self.cfg.rpn_stride * (y + h),
                     np.max(p_cls[0, ii, :])])

        for cls_num, box in boxes.items():
            boxes_nms = roi_helpers.non_max_suppression_fast(box, overlap_thresh=0.5)
            boxes[cls_num] = boxes_nms
            print(self.class_mapping[cls_num] + ":")
            for b in boxes_nms:
                b[0], b[1], b[2], b[3] = get_real_coordinates(ratio, b[0], b[1], b[2], b[3])
                print('{} prob: {}'.format(b[0: 4], b[-1]))
                one_time_dict["label"] = self.class_mapping[cls_num]
                one_time_dict["score"] = b[-1]
                one_time_dict["bbox"] = [b[0], b[1], b[2], b[3]]
                copy_dict = copy.copy(one_time_dict)
                dict_list.append(copy_dict)
        img = draw_boxes_and_label_on_image_cv2(img, self.class_mapping, boxes)
        print('Elapsed time = {}'.format(time.time() - tic))
        #pprint.pprint(dict_list)
            
        #cv2.imshow('image', img)
        #result_path = './results_images/{}.png'.format('result')
        #print('result saved into ', result_path)
        #cv2.imwrite(result_path, img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        return dict_list

    def detect_on_video(self, v):
        pass

