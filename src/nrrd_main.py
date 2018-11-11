"""
*****************************************************************************
*******************Ibrahim,CBICR,Tsinghua University*************************
*****************************************************************************
File name:    nrrd_main.py
Description:  nrrd main function
Author:       Ibrahim Yang
Version:      V1.0
Date:         2018-11-9
History:
*****************************************************************************
"""
from __future__ import print_function

import nrrd_convert
import os
import shutil

if __name__ == '__main__':
    my_nrrd_convert = nrrd_convert.nrrd_convert()

    dirpath = "/home/ibrahim/dataset/2018.9.21.yyl"
    savepath = "/home/ibrahim/dataset/2018.9.21.yyl_mat"
    img_path = "/home/ibrahim/dataset/2018.9.21.yyl_label"
    vision_path = "/home/ibrahim/dataset/2018.9.21.yyl_vision"
    txtpath = "/home/ibrahim/dataset/2018.9.21.yyl.txt"

    if os.path.exists(savepath):
        shutil.rmtree(savepath)
    if os.path.exists(img_path):
        shutil.rmtree(img_path)
    if os.path.exists(vision_path):
        shutil.rmtree(vision_path)

    os.makedirs(savepath)
    os.makedirs(img_path)
    os.makedirs(vision_path)

    my_nrrd_convert.nrrd_image2mat(origin_dir=dirpath, vision_dir=vision_path, save_dir=savepath, image_dir=img_path, txt_dir = txtpath)