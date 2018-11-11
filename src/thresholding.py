import cv2
import os
import nrrd
import scipy.io as scio
import numpy as np
import shutil
from PIL import Image

def nrrd_image2mat(dir, save_dir):
    # counter = 0
    nrrd_image = set(['png'])
    for root, dirs, files in os.walk(dir):
        for file in files:
            apath = os.path.join(root, file)
            if apath.split('.')[-1] in nrrd_image:
                img = cv2.imread(apath, 0)
                img = cv2.medianBlur(img, 5)
                # th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
                ret, th = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
                cv2.imwrite(save_dir + str(file), th)
                # cv2.imwrite(save_dir + 'binary_output/' + str(file), th)
                # cv2.imwrite(save_dir + 'origin_output/' + str(file), img)
                # counter += 1


if __name__ == '__main__':
    dirpath = "/home/deepliver/ibrahim/src/liverseg/results/seg_liver_ck/YC/"
    savepath = "/home/deepliver/Desktop/seg_liver/YC/"

    if os.path.exists(savepath):
        shutil.rmtree(savepath)
    os.makedirs(savepath)

    nrrd_image2mat(dirpath, savepath)

    # for folder_number in range(50, 51):
    #     folder_now = dirpath + str(folder_number) + '/'
    #     # path = os.listdir(folder_now)
    #     savepath_now = savepath + str(folder_number) + '/'
    #     os.makedirs(savepath + str(folder_number) + '/')
    #     nrrd_image2mat(folder_now, savepath_now)

