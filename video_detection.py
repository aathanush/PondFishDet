import cv2
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


path = input('Paste the path to the video file (use / instead of \\ )')


def generate_video(path,dest):
    image_folder = path
    video_name = dest

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")]

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 24, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        os.remove(os.path.join(image_folder, image))
    cv2.destroyAllWindows()
    video.release()


def FrameCapture(path,dest):
    vidObj = cv2.VideoCapture(path)
    count = 0
    success = 1

    while success:
        success, image = vidObj.read()
        if success==False:
            break
        cv2.imwrite(f"{dest}test_video{count}.jpg", image)

        count += 1

FrameCapture(path,'./detections/')

if choice.upper()=='CLAHE':
    CLAHE_algorithm('./detections/','./detections/')
else:
    MSR_algorithm('./detections/','./detections/')

generate_video('./detections/','./detections/test_video.avi')

model.predict('./detections/test_video.avi',save=True)
