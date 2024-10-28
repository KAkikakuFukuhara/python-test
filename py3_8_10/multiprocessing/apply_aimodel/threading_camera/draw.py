import tkinter as tk
import numpy as np
import cv2
    
def draw_object(image: np.ndarray, name: str, rect_wn: tuple,
                rect_es: tuple, score: float, color: list) -> np.ndarray:
    """　画像に検出物体の矩形を追加する
    !テスト済み
    """
    
    #draw box
    tl = round(0.002 * max(image.shape[0:2])) + 1
    cv2.rectangle(image, rect_wn, rect_es, color, thickness=tl)
    
    # draw text
    display_txt = "%s: %.lf%%" % (name, 100*score)
    tf = max(tl -1, 1)
    t_size = cv2.getTextSize(display_txt, 0, fontScale=tl / 3, thickness=tf)[0]
    rect_es = rect_wn[0] + t_size[0], rect_wn[1] - t_size[1] - 3
    cv2.rectangle(image, rect_wn, rect_es, color, -1)
    cv2.putText(image, display_txt, (rect_wn[0], rect_wn[1] - 2),
                0, tl / 3, [255, 255, 255], thickness=tf,
                lineType=cv2.LINE_AA)

    return image

def draw_center_pos(image: np.ndarray, rect_wn: tuple, rect_es: tuple, color: list) -> np.ndarray:
    cv2.rectangle(image, rect_wn, rect_es, color, -1)
    return image

def draw_objects(image: np.ndarray, objs: list) -> np.ndarray:
    """ 画像に複数の検出物体の矩形を追加する
    !テスト済み
    """
    draw_image = image.copy()
    for obj in objs:
        name = getattr(obj, "name")
        rect_wn = getattr(obj, "rect_wn")
        rect_es = getattr(obj, "rect_es")
        score = getattr(obj, "score")
        color = [0, 0, 255] if obj.is_nearest() else [180, 255, 255]
        draw_object(draw_image, name, rect_wn, rect_es, score, color)
        cw = getattr(obj, "cw")
        ch = getattr(obj, "ch")
        c_rect_wn = (cw - 2, ch - 2)
        c_rect_es = (cw + 2, ch + 2)
        draw_center_pos(draw_image, c_rect_wn, c_rect_es, color)

    return draw_image



        
