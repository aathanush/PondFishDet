from ultralytics import YOLO
import os
import sys
from img_enhancements.CLAHE.CLAHE import CLAHE_algorithm
from img_enhancements.CLAHE.sceneRadianceCLAHE import RecoverCLAHE
from img_enhancements.MSR.MSR import MSR_algorithm

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
directory=input('Paste the path to the directory containing the images (use / instead of \\ )')
if directory[-1]!='/':
    directory+='/'
result='./img_enhancements/'+choice+'/results/'
if choice=='CLAHE':
    CLAHE_algorithm(directory)
else:
    MSR_algorithm(directory)

images=os.listdir('./results/')
for i in images:
    res=model('./results/'+i)
    boxes=res[0].boxes
    annotations=[]

    for box in boxes:

        s='0 '
        plot=box.xyxyn
        for j in plot:
            s=s+str(j)+' '
        s+='\n'
        annotations.append(s)
    with open('./results/'+i[:-3]+'txt','w') as file:
        os.remove('./results/'+i)
        file.writelines(annotations)
print(f"The annotations are saved in ./results/")