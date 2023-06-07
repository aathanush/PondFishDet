import os
import numpy as np
import cv2

def CLAHE_algorithm(path,dest):
    from img_enhancements.CLAHE.sceneRadianceCLAHE import RecoverCLAHE
    np.seterr(over='ignore')
    l=os.listdir(path)
    count=0
    for file in l:
        image = cv2.imread(path+file)
        sceneRadiance = RecoverCLAHE(image)
        cv2.imwrite(dest+file, sceneRadiance)
        if round(count/len(l)*100)%10==0:
            print(count/len(l)*100, "% complete")
        count+=1

