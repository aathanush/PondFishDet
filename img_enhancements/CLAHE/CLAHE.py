import os
import numpy as np
import cv2

def CLAHE_algorithm(path,dest):

    np.seterr(over='ignore')
    print("CLAHE Image Enhncement algorithm loaded")
    l=os.listdir(path)
    print(l)
    count=0
    for file in l:
        image = cv2.imread(path+file)
        sceneRadiance = RecoverCLAHE(image)
        cv2.imwrite(dest+file, sceneRadiance)
        if (count/len(l)*100)%10==0:
            print(count/len(l)*100, "% complete")
        count+=1

