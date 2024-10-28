import os

config = {}

##### Share param #####
config['share'] = {}
# network setting
config['share']['pool_size'] = 14
config['share']['stride'] = 16
# anchor param
config['share']['anc_scales'] = [64, 128, 256]
config['share']['anc_ratios'] = [[1, 1], [1, 2], [2, 1]]
# image preprocessing 
config['share']['input_img_min_size'] = 600
config['share']['image_channel_mean'] = [123.68, 116.779, 103.939]
config['share']['image_channel_std'] = 1.0
# rpn param
config['share']['rpn_std_scaling'] = 4.0
config['share']['rpn_reg_mean'] = [0.0, 0.0, 0.0, 0.0]
config['share']['rpn_reg_std'] = [1.0, 1.0, 1.0, 1.0]
# roi param
config['share']['roi_reg_mean'] = [0.0, 0.0, 0.0, 0.0]
config['share']['roi_reg_std'] = [0.1, 0.1, 0.2, 0.2]
# label mapping
config['share']['label_mapping'] = None

##### Training param #####
config['train'] = {}
# making rpn target param
config['train']['rpn_max_iou'] = 0.7
config['train']['rpn_min_iou'] = 0.3
# making roi target param
config['train']['roi_max_iou'] = 0.5
config['train']['roi_min_iou'] = 0.1
config['train']['num_use_rois'] = 64
# ploposal layer param
config['train']['nms_iou'] = 0.7
config['train']['num_nms_boxes'] = 2000

##### Test Param #####
config['test'] = {}
# ploposal layer param
config['test']['nms_iou'] = 0.7
config['test']['num_use_rois'] = 300
config['test']['num_nms_boxes'] = 300
