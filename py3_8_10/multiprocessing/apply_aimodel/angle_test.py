import cameras
import time
import os

camera = cameras.CameraWithIMU()
sleep_time = 0.7
sleep_freq = 50
sleep_start_flag = False

try:
    camera.start()
    gs = time.time()
    s = time.time()
    text = []
    while True:
        e = time.time()
        if e - gs > 30:
            break

        if e - gs > 10 and not sleep_start_flag :
            sleep_start_flag = True
            s = time.time()

        if (e - s) > sleep_freq and sleep_start_flag:
            time.sleep(sleep_time)
            s = time.time()
            flag = "F"
        else:
            flag = "T"

        camera.update_frames()
        r, p, y = camera.get_camera_angles()
        angles = f"flag:{flag},Time:{e - gs},Roll:{r:.2f}, PITCH:{p:.2f}, YAW:{y:.2f}"
        print(angles)
        text.append(angles)
finally:
    camera.stop()

texts = "\n".join(text)
with open(f"{os.path.dirname(__file__)}/angle_s{'_'.join(str(sleep_time).split('.'))}_f{sleep_freq}.txt", "w") as f:
    print("save")
    f.write(texts)

    
