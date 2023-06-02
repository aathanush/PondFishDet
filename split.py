import os
from random import choice
import shutil

#arrays to store file names
imgs =[]
xmls =[]

#setup dir names
trainPath = r"E:\Working_Projects\DePondFI\Single-Underwater-Image-Enhancement-and-Color-Restoration\Underwater-Image-Enhancement\CLAHE\Dataset\train"
valPath = r"E:\Working_Projects\DePondFI\Single-Underwater-Image-Enhancement-and-Color-Restoration\Underwater-Image-Enhancement\CLAHE\Dataset\valid"
crsPath = r"E:\Working_Projects\DePondFI\Single-Underwater-Image-Enhancement-and-Color-Restoration\Underwater-Image-Enhancement\CLAHE\CLAHE_train_dataset" #dir where images and annotations stored

#setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
train_ratio = 0.8
val_ratio = 0.2


#total count of imgs
totalImgCount = len(os.listdir(crsPath))/2

#soring files to corresponding arrays
for (dirname, dirs, files) in os.walk(crsPath):
    for filename in files:
        if filename.endswith('.txt'):
            xmls.append(filename)
        else:
            imgs.append(filename)


#counting range for cycles
countForTrain = int(len(imgs)*train_ratio)
countForVal = int(len(imgs)*val_ratio)
print("training images are : ",countForTrain)
print("Validation images are : ",countForVal)



trainimagePath = 'E:\Detection of Garbage  Litterer\yolov5-mainTraffic Sign\DATASET\train\images'
trainlabelPath = 'E:\Detection of Garbage  Litterer\yolov5-mainTraffic Sign\DATASET\train\labels'
valimagePath = 'E:\Detection of Garbage  Litterer\yolov5-mainTraffic Sign\DATASET\test\images'
vallabelPath = 'E:\Detection of Garbage  Litterer\yolov5-mainTraffic Sign\DATASET\test\labels'
#cycle for train dir
for x in range(countForTrain):

    fileJpg = choice(imgs) # get name of random image from origin dir
    fileXml = fileJpg[:-4] +'.txt' # get name of corresponding annotation file

    #move both files into train dir
    #shutil.move(os.path.join(crsPath, fileJpg), os.path.join(trainimagePath, fileJpg))
    #shutil.move(os.path.join(crsPath, fileXml), os.path.join(trainlabelPath, fileXml))
    shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(trainimagePath, fileJpg))
    shutil.copy(os.path.join(crsPath, fileXml), os.path.join(trainlabelPath, fileXml))


    #remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)



#cycle for test dir   
for x in range(countForVal):

    fileJpg = choice(imgs) # get name of random image from origin dir
    fileXml = fileJpg[:-4] +'.txt' # get name of corresponding annotation file

    #move both files into train dir
    #shutil.move(os.path.join(crsPath, fileJpg), os.path.join(valimagePath, fileJpg))
    #shutil.move(os.path.join(crsPath, fileXml), os.path.join(vallabelPath, fileXml))
    shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(valimagePath, fileJpg))
    shutil.copy(os.path.join(crsPath, fileXml), os.path.join(vallabelPath, fileXml))
    
    #remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)

#rest of files will be validation files, so rename origin dir to val dir
#os.rename(crsPath, valPath)
shutil.move(crsPath, valPath) 
