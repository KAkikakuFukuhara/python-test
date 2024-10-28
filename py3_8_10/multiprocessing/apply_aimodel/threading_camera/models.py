""" 物体検出クラス
"""
import time

import config
from detector import FasterRCNNDetector


class DetectionObject:
    def __init__(self, name, rect_wn, rect_es, score):
        self.name = name
        self.rect_wn = rect_wn
        self.rect_es = rect_es
        self.score = score
        self.depth = 0.0
        self.nearest_flag = False
        self.w_dist = 0.0
        self.h_dist = 0.0
        self.d_dist = 0.0

        # cw is center_width. ch is center_height. 
        self.cw = rect_wn[0] + (( rect_es[0] - rect_wn[0] ) // 2) 
        self.ch = rect_wn[1] + (( rect_es[1] - rect_wn[1] ) // 2)

    def is_nearest(self) -> bool:
        return self.nearest_flag
        
class Model:
    def __init__(self):
        self.model = FasterRCNNDetector(model_path="my_best_model_greenback.hdf5")
        self.coconames = config.coconames
        self.names_colors = config.names_colors

        # 保持状態
        self.detect_objects_name = []
        self.detect_objects = []
        self.detect_time = None

    def detect(self, image):
        # 保持している検出物体情報の初期化
        self.detect_objects_name = []
        self.detect_objects = []

        # >> 物体検出 ここから
        print("### Dtection Start")
        start = time.time()
        output = self.model.detect_on_image(image)

        # 検出物体インスタンスの作成
        for i, o in enumerate(output):
            box = o["bbox"]
            label = o["label"]
            score = o["score"]
            if score > 0.5:
                label_name = "{}:{}".format(i, label)
                box_wn = ( int(box[0]), int(box[1]) )
                box_es = ( int(box[2]), int(box[3]) )
                self.detect_objects_name.append(label_name)
                self.detect_objects.append(DetectionObject(label_name, box_wn, box_es, score))

        end = time.time()
        # <<　物体検出ここまで
        
        detect_time = end - start
        self.detect_time = "{:.3f}s".format(detect_time)
        print("### Detection Stop")

    def get_detect_objects_name(self) -> dict:
        return self.detect_objects_name

    def get_detect_objects(self) -> list:
        return self.detect_objects

    def get_detect_time(self) -> str:
        return self.detect_time

        
        
    

