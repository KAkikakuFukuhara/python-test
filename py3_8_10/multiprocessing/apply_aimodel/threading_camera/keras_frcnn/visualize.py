import cv2
import numpy as np
import colorsys



def _create_unique_color_float(tag, hue_step=0.41):

    h, v = (tag * hue_step) % 1, 1.0 - (int(tag * hue_step) % 4) / 5.0
    r, g, b = colorsys.hsv_to_rgb(h, 1.0, v)

    return r, g, b



def _create_unique_color_uchar(tag, hue_step=0.41):

    r, g, b = _create_unique_color_float(tag, hue_step)

    return int(255 * r), int(255 * g), int(255 * b)



def draw_boxes_and_label_on_image_cv2(img, class_label_map, class_boxes_map):

    for c, boxes in class_boxes_map.items():
        for box in boxes:
            assert len(box) == 5, 'class_boxes_map every item must be [bb_left, bb_top, bb_width, bb_height, prob]'

            bb_left = int(box[0])
            bb_top = int(box[1])
            bb_width = int(box[2])
            bb_height = int(box[3])

            prob = round(box[4], 2)
            unique_color = _create_unique_color_uchar(c)
            cv2.rectangle(img, (bb_left, bb_top), (bb_width, bb_height), unique_color, 2)

            text_label = '{}{}'.format(class_label_map[c], prob)
            (ret_val, base_line) = cv2.getTextSize(text_label, cv2.FONT_HERSHEY_COMPLEX, 1, 1)
            text_org = (bb_left, bb_top - 0)

            cv2.rectangle(img, (text_org[0] - 5, text_org[1] + base_line - 5),
                          (text_org[0] + ret_val[0] + 5, text_org[1] - ret_val[1] + 5),
                          unique_color, -1)
            cv2.putText(img, text_label, text_org, cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

    return img



def visualize_det_cv2(img, detections, classes=None, thresh=0.6):

    assert classes, 'from visualize_det_cv2, classes must be provides, each class in a list with certain order.'
    assert isinstance(img, np.array), 'from visualize_det_cv2, img must be a numpy array object.'

    height = img.shape[0]
    width = img.shape[1]

    for i in range(detections.shape[0]):
        cls_id = int(detections[i, 0])
        if cls_id >= 0:
            score = detections[i, 1]
            if score > thresh:
                unique_color = _create_unique_color_uchar(cls_id)

                x1 = int(detections[i, 2] * width)
                y1 = int(detections[i, 3] * height)
                x2 = int(detections[i, 4] * width)
                y2 = int(detections[i, 5] * height)

                cv2.rectangle(img, (x1, y2), (x2 - x1, y2 - y1), unique_color, 2)

                text_label = '{} {}'.format(classes[cls_id], score)
                (ret_val, base_line) = cv2.getTextSize(text_label, cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                text_org = (x1, y2 - 0)

                cv2.rectangle(img, (text_org[0] - 5, text_org[1] + base_line - 5),
                              (text_org[0] + ret_val[0] + 5, text_org[1] - ret_val[1] + 5), unique_color, 2)

                cv2.rectangle(img, (text_org[0] - 5, text_org[1] + base_line - 5),
                              (text_org[0] + ret_val[0] + 5, text_org[1] - ret_val[1] + 5), unique_color, -1)

                cv2.putText(img, text_label, text_org, cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

    return img
