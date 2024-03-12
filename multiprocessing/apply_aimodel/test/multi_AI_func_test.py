import multiprocessing 
import time

import numpy as np 
import tensorflow as tf

def make_model() -> tf.keras.Model:
    """
    """
    input_layer = tf.keras.layers.Input(shape=(480, 640, 3), name="input")
    x = tf.keras.layers.Conv2D(8, 3, activation='relu', padding="same", name="conv1_1")(input_layer)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv1_2")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv1_3")(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(4, 4), name="pool1")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv2_1")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv2_2")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv2_3")(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(4, 4), name="pool2")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv3_1")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv3_2")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv3_3")(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(4, 4), name="pool3")(x)
    x = tf.keras.layers.Flatten(name="flatten")(x)
    x = tf.keras.layers.Dense(512, activation="relu", name="linear1")(x)
    x = tf.keras.layers.Dense(10, activation="softmax", name="linear2")(x)

    model = tf.keras.Model(inputs=input_layer, outputs=x)
    model.summary()
    return model

def func_np(r_queue:multiprocessing.Queue, s_queue:multiprocessing.Queue) -> None:
    """
    """
    model = make_model()

    start = time.time()
    while True:
        # 終了保険 (3分経過で終了)
        elapsed_time = time.time() - start
        if elapsed_time > 180:
            break

        # queueにimageが入るまで待つ
        if r_queue.empty():
            continue

        image = r_queue.get()
        print(type(image))
        result = model(image)
        argmax = tf.keras.backend.argmax(result).numpy()
        s_queue.put(argmax.tolist())


def main():
    """
    """
    image = np.random.randint(0, 255, (1, 480, 640, 3)).astype("float32") / 255
    s_queue = multiprocessing.Queue()
    r_queue = multiprocessing.Queue()
    ppe = multiprocessing.Process(target=func_np, daemon=True, args=(s_queue, r_queue))
    ppe.start()
    s_queue.put(image)
    start = time.time()
    i = 0
    while True:
        elapsed_time = time.time() - start
        if elapsed_time > 60:
            break

        if r_queue.empty():
            continue

        result = r_queue.get()
        print(result)
        break


if __name__ == "__main__":
    main()
