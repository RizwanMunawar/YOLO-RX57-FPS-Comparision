## Object Detection Algorithms YOLO Series [Suppport for Windows & Linux]

### FPS-Comparision-YOLO-Series

- Leading YOLO Series Algorithms FPS Comparision with same specifications.
- The comparision include, YOLOv7, YOLOv5, YOLOX, YOLO-R


### Recommended Envirnoment
- Operating System : Ubuntu 18/Ubuntu 20/Windows 10
- python 3.6/3.7/3.8

### Output
https://user-images.githubusercontent.com/62513924/182783948-8e2ddb62-ddf7-4970-9aab-56ce2d45d2ed.mp4
### Start Guide


[`yolor_p6.pt`](https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.3-release/yolor_p6.pt) 
[`yolov5s.pt`](https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.3-release/yolov5s.pt) 
[`yolov7.pt`](https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.3-release/yolov7.pt) 
[`yolox_s.pth`](https://github.com/RizwanMunawar/YOLO-RX57-FPS-Comparision/releases/download/v0.1.3-release/yolox_s.pth) 


- Basic usage
```
python3 comparision.py --source "2.mp4" --device 0
```
or
```
python3 comparision.py --source "2.mp4" --device cpu
```
##### The above command will store the output of all detectors in a new folder named results. The results folder will contain output videos for every object detector, FPS will be shown on every video.

### Custom Weights
```
python3 comparision.py --source "2.mp4" --device 0 --yolov5weights yolov5s.pt --yolorweights yolor_p6.pt --yoloxweights yolox_s.pt --yolov7weights yolov7.pt
```
![Results Folder Look....!](https://user-images.githubusercontent.com/62513924/183150516-664cf061-a0f5-46a8-a4d8-8655eccc6d60.png)


### Coming Soon
- histogram plot for fps comparision every second
- Merge output video into single video side-by-side
- 
For more details, you can reach out to me on [Medium](https://chr043416.medium.com/) or can connect with me on [LinkedIn](https://www.linkedin.com/in/muhammadrizwanmunawar/)
