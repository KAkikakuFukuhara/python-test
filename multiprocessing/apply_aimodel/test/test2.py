import ctypes
import multiprocessing as mp
import numpy as np
import random
from concurrent.futures import ProcessPoolExecutor
import matplotlib.pyplot as plt
import time

def value_to_ndarray(v:mp.Value) -> np.ndarray:
    n = np.ctypeslib.as_array(v.get_obj())
    return n

def ndarray_to_value(n:np.ndarray) -> mp.Value:
    assert len(n.shape) == 3
    n_h, n_w, n_ch = n.shape
    v = mp.Value(ctypes.c_uint8 * n_ch * n_w * n_h)
    value_to_ndarray(v)[:] = n
    return v

def ndarray_to_ctypes(n:np.ndarray) -> ctypes.Array:
    assert len(n.shape) == 3
    n_h, n_w, n_ch = n.shape
    c = (ctypes.c_uint8 * n_ch * n_w * n_h)()
    new_n = ctypes_to_ndarray(c)
    new_n[:] = n
    return c

def ctypes_to_ndarray(c) -> np.ndarray:
    n = np.ctypeslib.as_array(c)
    return n

def make_rectangle(v_image:mp.Value) -> mp.Value:
    org_image = value_to_ndarray(v_image)
    edit_image = org_image.copy()
    # image processing
    edit_image = ( edit_image + [255, 255, 0] ) / 2
    edit_image = edit_image.astype("uint8")
    org_image[:] = edit_image
    return v_image

def make_rectangle2(c):
    org_image = ctypes_to_ndarray(c)
    edit_image = org_image.copy()
    # image processing
    edit_image = ( edit_image + [255, 255, 0] ) / 2
    edit_image = edit_image.astype("uint8")
    return ndarray_to_ctypes(edit_image)

def make_rectangle3(l:list) -> np.ndarray:
    org_image = np.array(l)
    edit_image = org_image.copy()
    # image processing
    edit_image = ( edit_image + [255, 255, 0] ) / 2
    edit_image = edit_image.astype("uint8")
    return edit_image.tolist()

def make_rectangle4(n:np.ndarray) -> np.ndarray:
    time.sleep(1)
    print(type(n))
    org_image = n
    edit_image = org_image.copy()
    # image processing
    edit_image = ( edit_image + [255, 0, 255] ) / 2
    edit_image = edit_image.astype("uint8")
    return edit_image


def make_image() -> np.ndarray:
    image = np.random.randint(0, 255, (480, 640, 3))
    return image

def main():
    result = None
    image = make_image()
    plt.imshow(image)
    plt.show()
    p = ProcessPoolExecutor()
    future = p.submit(make_rectangle4, image)
    while True:
        try:
            if future.done():
                result = future.result()
                print("finish")
                break
            else:
                print("mada")
        except KeyboardInterrupt:
            break
    if result is not None:
        result = np.array(result)
        plt.imshow(result)
        plt.show()

if __name__ == "__main__":
    main()
