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

import sys
sys.path.append("..")
import nrrd_convert
import os
import shutil

"""
Function:     main
Description:  convert nrrd image to ./mat ./label ./vision ./txt
Calls:        nrrd_convert
Called By:    none
Input:        none
Output:       none
Return:       ./*mat ./*label ./*vision ./*txt
Others:       none
"""
if __name__ == '__main__':
    my_nrrd_convert = nrrd_convert.nrrd_convert()

    dirpath =       "/home/deepliver/ibrahim/dataset/100235663/100235663"
    savepath =      "/home/deepliver/ibrahim/dataset/100235663/100235663_mat"
    img_path =      "/home/deepliver/ibrahim/dataset/100235663/100235663_label"
    vision_path =   "/home/deepliver/ibrahim/dataset/100235663/100235663_vision"
    txtpath =       "/home/deepliver/ibrahim/dataset/100235663/100235663.txt"

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