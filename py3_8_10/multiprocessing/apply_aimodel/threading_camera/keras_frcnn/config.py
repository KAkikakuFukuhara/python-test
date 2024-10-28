from tensorflow.keras import backend as K
import math

class Config:
    def __init__(self):
        self.verbose = True

        self.network = 'resnet50'

        # 学習データ増強用オプション　のオンオフ
        self.use_horizontal_flips = False
        self.use_vertical_flips = False
        self.rot_90 = False

        # アンカーボックスのスケール
        self.anchor_box_scales = [32, 64, 128, 256] #[128, 256, 512]

        # アンカーボックスの比率
        self.anchor_box_ratios = [[1, 1], [1./math.sqrt(2), 2./math.sqrt(2)], [2./math.sqrt(2), 1./math.sqrt(2)]]

        # 画像リサイズ時の短辺
        self.im_size = 480

        # 減算用の平均画像
        self.img_channel_mean = [103.939, 116.779, 123.68]
        self.img_scaling_factor = 1.0

        # 一度に計算するROI（実質のバッチサイズ）
        self.num_rois = 4

        # rpn層が出力する特徴マップと元画像の縮小率
        self.rpn_stride = 16

        self.balanced_classes = False #なんだよこれは

        # 座標変換用のスケール　なんでここはrpn_strideと違うんだろうね
        self.std_scaling = 4.0
        self.classifier_regr_std = [8.0, 8.0, 4.0, 4.0]

        # ground_truthとのIoUしきい値
        self.rpn_min_overlap = 0.3
        self.rpn_max_overlap = 0.7

        # NMS用のIoUしきい値
        self.classifier_min_overlap = 0.1
        self.classifier_max_overlap = 0.5

        self.class_mapping = None
        self.val_class_mapping = None

        # 学習済みモデルのpath
        self.model_path = "./my_best_model.hdf5"

        # データの場所
        self.data_dir = './data' # これどこで使ってんの？

        # 学習するエポック数
        self.num_epochs = 30

        # これもどこで使われてるかわからない
        self.kitti_simple_label_file = 'apple_annotations.txt'

        # アノテーション情報　画像のpath,x1,y1,x2,y2,label　で並んでる
        self.simple_label_file = 'apple_annotations.txt'
        self.val_label_file = 'real_apple_annotations.txt'

        # 設定ファイルを保存するときのファイル名
        self.config_save_file = 'config.pickle'
        
        # 学習済みモデルの場所（ファイル名を除く　なんで除いてるのかは知らん trainで指定しなおしてるので変数宣言以上の意味はなさそう）
        self.base_net_weight = "./"
