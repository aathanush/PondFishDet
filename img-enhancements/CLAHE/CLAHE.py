import os
import numpy as np
import cv2
import natsort
import xlwt
from skimage import exposure

from sceneRadianceCLAHE import RecoverCLAHE
from sceneRadianceHE import RecoverHE
np.seterr(over='ignore')


path = r"D:\hello\books\python\MiniProject\dataset\yolov5\DePondFI23\DePondFI23\test\images"
path1 = r"D:\hello\books\python\Single-Underwater-Image-Enhancement-and-Color-Restoration\Underwater Image Enhancement\CLAHE\test"
os.chdir(path)

for file in os.listdir():
    if file.endswith(".jpg"):
        image = cv2.imread(file)

        print(image.shape)

        sceneRadiance = RecoverCLAHE(image)
        #sceneRadiance = RecoverGC(image)
        print("--- ")

        #cv2_imshow(image_salient_1)
        os.chdir(path1)
        cv2.imwrite(file, sceneRadiance)
        os.chdir(path)