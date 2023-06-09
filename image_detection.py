from ultralytics import YOLO
import os
import sys
from img_enhancements.CLAHE.CLAHE import CLAHE_algorithm
from img_enhancements.CLAHE.sceneRadianceCLAHE import RecoverCLAHE
from img_enhancements.MSR.MSR import MSR_algorithm
import time
import natsort
import xlwt
from skimage import exposure
k=os.listdir('./detections/')
for i in k:
    os.remove('./detections/'+i)

choice=''
choice=input('Which Image enhancement algorithm would you like to choose? ( MSR / CLAHE )')
if choice.upper()=='CLAHE':
    model = YOLO('weights/CLAHE_yolov8s.pt')
elif choice.upper()=='MSR':
    model = YOLO('weights/MSR_yolov8s.pt')
else:
    print("Invalid choice! Please run the script again!")
    sys.exit()


print("Model loaded")


path = input('Paste the path to the directory containing images(s) (use / instead of \\ )')


print(f"Performing {choice} image processing")
if choice.upper()=='CLAHE':
    CLAHE_algorithm(path,'./detections/')
else:
    MSR_algorithm(path,'./detections/')

images=os.listdir('./detections/')
for i in images:
    model.predict('./detections/'+i,save=True)
for i in os.listdir('./detections/'):
    os.remove(f"./detections/{i}")

