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

if choice.upper()=='CLAHE':
    CLAHE_algorithm(path,'./detections/')
else:
    MSR_algorithm(path,'./detections/')

now=time.time()
images=os.listdir('./detections/')
for i in images:
    model.predict('./detections/'+i,save=True)
after = time.time()
for i in os.listdir('./detections/'):
    os.remove(f"./detections/{i}")
print(1000*(after-now))

