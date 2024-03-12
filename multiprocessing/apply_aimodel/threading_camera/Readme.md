# スレッドとマルチプロセスを用いた映像処理

## 概要

カメラをスレッドで走らせqueue.Queueにフレームを送信し続ける。
メインスレッドはQueueからフレームを受信してGUIに表示する。
マルチプロセスで物体検出を行う

## 環境

* Ubuntu 18.04 LTS
* Anaconda
* python 3.7
<br>

* pyrealsense2
* numpy
* tensorflow-cpu
* python-opencv

## 仕様

### スレッドで動作するカメラ