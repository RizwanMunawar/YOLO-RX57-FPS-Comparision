import os
import sys
import shutil
import argparse
import platform
from pathlib import Path

#run function
def run(
        yolov5weights='yolov5s.pt',    #yolov5 detection weights
        yolorweights='yolor_p6.pt',    #yolor detection weights
        yoloxweights='yolox_s.pth',    #yolox detection weights
        yolov7weights='yolov7.pt',     #yolov7 detection weights
        source='data/images',          #images/video/webcam
        imgsize= 640,                  #imagesize
        conf_thres=0.25,               #confidence threshold
        iou_thres=0.45,                #iou_threshold
        device='',                     #devices
        ):    


    #output directory for storing results
    outputdir = "results"
    if not os.path.exists(outputdir):
        os.mkdir(outputdir)

    
    #.................................YOLOv5..................................
    #current directory in which script exists and move to yolov5 directory
    original_file_path = os.getcwd()
    os.chdir("YOLOv5Research/yolov5")

    #installation of requirements file
    os.system('pip install -r requirements.txt')

    #basic information
    print("\n..........YOLOV5 SPECS................")
    print("YOLOv5 Weights : ", yolov5weights)
    print("YOLOv5 Source : ",source)
    print("Image Size : ", imgsize)
    print("......................................\n")

    #detection subcommand
    os.system('python3 detect_fps.py \
                        --weights {} \
                        --source {} \
                        --imgs {} \
                        --conf-thres {} \
                         --iou-thres {} \
                         --device {}'.format(yolov5weights,
                         source,imgsize,conf_thres,iou_thres,device))


    #move output to main folder
    for fil in os.listdir("runs/detect/exp/"):
        shutil.move(("runs/detect/exp/"+fil),("../../results/"+fil))
    
    #remove output folder for yolov5 export
    shutil.rmtree("runs/detect/exp")
    #........................................................................


    #.................................YOLOR..................................
    #current directory in which script exists and move to yolor directory
    os.chdir(original_file_path)
    os.chdir("YOLORResearch/yolor")

    #installation of requirements file
    os.system('pip install -r requirements.txt')
    
    #print basic information
    print("\n..........YOLOR SPECS................")
    print("YOLOR Weights : ", yolorweights)
    print("YOLOR Source : ",source)
    print("Image Size : ", imgsize)
    print("......................................\n")
 

    #detection subcommand
    os.system('python3 detect_fps.py --weights {} --source {} --img-size {} \
                --conf-thres {} --iou-thres {} --device {}'.format(yolorweights,source,imgsize,conf_thres,iou_thres,device))

    #move output to main folder
    for fil in os.listdir("inference/output/"):
        shutil.move(("inference/output/"+fil),("../../results/"+fil))
    
    #remove output folder for yolov5 export
    shutil.rmtree("inference/output/")

    #.................................YOLOv7..................................
    #get current directory in which script exists and move to yolov5 directory
    os.chdir(original_file_path)
    os.chdir("YOLOv7Research/yolov7")

    #installation of requirements file
    os.system('pip install -r requirements.txt')
    
    #print basic information
    print("\n..........YOLOv7 SPECS................")
    print("YOLOv7 Weights : ", yolov7weights)
    print("YOLOv7 Source : ",source)
    print("Image Size : ", imgsize)
    print("......................................\n")

    #detection subcommand
    os.system('python3 detect_fps.py --weights {} --source {} --img-size {} \
                --conf-thres {} --iou-thres {} --device {} --no-trace'.format(yolov7weights,source,imgsize,conf_thres,iou_thres,device))


    #move output to main folder
    for fil in os.listdir("runs/detect/exp/"):
        shutil.move(("runs/detect/exp/"+fil),("../../results/"+fil))
    
    # remove output folder for yolov7 export
    shutil.rmtree("runs/detect/exp")

    
    #.................................YOLOX..................................
    #get current directory in which script exists and move to yolov5 directory
    os.chdir(original_file_path)
    os.chdir("YOLOXResearch/YOLOX")

    #installation of requirements file
    os.system('pip3 install -v -e .')

    #print basic information
    print("\n..........YOLOX SPECS................")
    print("YOLOX Weights : ", yoloxweights)
    print("YOLOX Source : ",source)
    print("Image Size : ", imgsize)
    print("......................................\n")

     #detection subcommand
    os.system('python3 tools/demo_fps.py video \
                                -n yolox-s \
                                -c {} \
                                 --path {}  \
                                 --conf {} \
                                 --nms {} \
                                 --tsize {} \
                                 --save_result \
                                 --device {}'.format(yoloxweights,source,conf_thres,iou_thres,imgsize,device))


    #move output to main folder
    for fil in os.listdir("output/exp"):
        shutil.move(("output/exp/"+fil),("../../results/"+fil))
    
    #remove output folder for yolov5 export
    shutil.rmtree("output/exp")


    os.chdir(original_file_path)
    
#parse basic arguments
def parse_opt():

    parser = argparse.ArgumentParser()
    parser.add_argument('--yolov5weights', nargs='+', type=str, default='yolov5s.pt', help='yolov5 model path(s)')
    parser.add_argument('--yolorweights', nargs='+', type=str, default='yolor_p6.pt', help='yolor model path(s)' )
    parser.add_argument('--yoloxweights', nargs='+', type=str, default='yolox_s.pth', help='yolox model path(s)' )
    parser.add_argument('--yolov7weights', nargs='+', type=str, default='yolov7.pt', help='yolov7 model path(s)')
    parser.add_argument('--source', type=str, required=True, help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--imgsize', nargs='+', type=int, default=640, help='inference size h,w')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--device', required=True, help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    opt = parser.parse_args()
    return opt


def main(opt):
    run(**vars(opt))

#main function call
if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
