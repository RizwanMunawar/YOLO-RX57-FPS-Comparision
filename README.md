# Official Implementation of SIGPRO 2022 Conference Paper  
*Published in the 8th International Conference on Signal and Image Processing (SIGPRO 2022), Toronto, Canada.*

## Paper Title
**[YOLOv5, YOLOX, YOLOR, and YOLOv7 Performance Comparison: A Survey](https://aircconline.com/csit/papers/vol12/csit121602.pdf)**

### Lead Authors
- [Saira Gillani](https://www.linkedin.com/in/saira-gillani/)
- [Muhammad Rizwan Munawar](https://pk.linkedin.com/in/muhammadrizwanmunawar)

## Overview
This repository provides the official code to compare FPS (frames per second) of various YOLO object detection algorithms (YOLOv5, YOLOX, YOLOR, and YOLOv7) under the same conditions. This comparison includes support for both Windows and Linux environments.

## FPS Comparison of YOLO Series
Compare the FPS of leading YOLO series algorithms with identical hardware specifications, enabling a clearer understanding of performance differences across versions.

### Recommended Envirnoment
- Operating System : Ubuntu 18/Ubuntu 20/Windows 10
- python 3.6/3.7/3.8

### Results
<img src= "/assets/results.png" style ="width:640px;height:360px;">

### Start Guide

#### For Ubuntu
```
git clone https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision.git
cd YOLO-RX57-FPS-Comparision
pip install Cython opencv-python
sudo apt update
sudo apt install build-essential
sudo apt-get install manpages-dev
pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
```
- Now you will need to download weights of YOLOR, YOLOv7 and YOLOX and move downloaded weights into respective folders using mentioned commands below.
```
cd YOLORResearch/yolor
wget https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.4-release/yolor_p6.pt
cd ..
cd ..
cd YOLOXResearch/YOLOX
wget https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.4-release/yolox_s.pth
cd ..
cd ..
wget YOLOv7Research/yolov7
wget https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.4-release/yolov7.pt
cd ..
cd ..
```
- Now you can run code with mentioned command below.
```
python3 comparision.py --source "2.mp4" --device 0

or

python3 comparision.py --source "2.mp4" --device cpu
```
- In above command, source will be the path of your video/image on, which you want to calculate FPS. 
##### The above command will store the output of all detectors in a new folder named results. The results folder will contain output videos for every object detector, FPS will be shown on every video.

- If you want to use your custom weights, you can use mentioned command below.
```
python3 comparision.py --source "2.mp4" --device 0 \
                       --yolov5weights yolov5s.pt --yolorweights yolor_p6.pt \
                       --yoloxweights yolox_m.pt --yolov7weights yolov7.pt
```

#### For Windows 10
```
git clone https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision.git
cd YOLO-RX57-FPS-Comparision
pip install pycocotools-windows
```

Now you will need to download weights of YOLOR, YOLOv7 and YOLOX and move downloaded weights into respective folders. Mentioned steps below to complete this.
- Download [yolor_p6.pt](https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.4-release/yolor_p6.pt) file and move the downloaded file in <b>YOLORResearch/yolor</b> folder
- Download [yolov7.pt](https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.4-release/yolov7.pt) file and move the downloaded file in <b>YOLOv7Research/yolov7</b> folder
- Download [yolox_s.pth](https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.4-release/yolox_s.pth) file and move the downloaded file in <b>YOLOXResearch/YOLOX</b> folder

Now you can run code with mentioned command below.
```
python3 comparision.py --source "2.mp4" --device 0

or

python3 comparision.py --source "2.mp4" --device cpu
```
- In above command, source will be the path of your video/image on which you want to calculate FPS. 
##### The above command will store the output of all detectors in a new folder named results. The results folder will contain output videos for every object detector, FPS will be shown on every video.

- If you want to use your custom weights, you can use mentioned command below.
```
python3 comparision.py --source "2.mp4" --device 0 \
                      --yolov5weights yolov5s.pt --yolorweights yolor_p6.pt \
                      --yoloxweights yolox_m.pt --yolov7weights yolov7.pt
```

### Coming Soon
- histogram plot for fps comparision every second
- Merge output video into single video side-by-side

### References
- https://github.com/ultralytics/yolov5
- https://github.com/WongKinYiu/yolor
- https://github.com/Megvii-BaseDetection/YOLOX
- https://github.com/WongKinYiu/yolov7

For more details, you can reach out to me on [Medium](https://chr043416.medium.com/) or can connect with me on [LinkedIn](https://www.linkedin.com/in/muhammadrizwanmunawar/)
