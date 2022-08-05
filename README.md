## Object Detection Algorithms YOLO Series
### FPS-Comparision-YOLO-Series

- Leading YOLO Series Algorithms FPS Comparision with same specifications.
- The comparision include, YOLOv7, YOLOv5, YOLOX, YOLO-R

### Output

### Start Guide


[`yolov7.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) 
[`yolov7x.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt) 
[`yolov7-w6.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6.pt) 
[`yolov7-e6.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6.pt) 
[`yolov7-d6.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-d6.pt) 
[`yolov7-e6e.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt)

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



For more details, you can reach out to me on [Medium](https://chr043416.medium.com/) or can connect with me on [LinkedIn](https://www.linkedin.com/in/muhammadrizwanmunawar/)

