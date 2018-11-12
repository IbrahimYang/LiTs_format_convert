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
import time

"""
Function:     main
Description:  convert nrrd image to ./mat ./label ./vision ./txt
Calls:        nrrd_convert
Called By:    none
Input:        none
Output:       none
Return:       ./*.mat ./*.label ./*.vision ./*.txt
Others:       none
"""
if __name__ == '__main__':
    standard_adress = 1
    if standard_adress:
        dir_path = "../liver_database/1-input_nrrd"
        save_path = "../liver_database/2-output_volumes/mat"
        img_path = "../liver_database/2-output_volumes/label"
        vision_path = "../liver_database/2-output_volumes/vision"
        txt_path = "../liver_database/2-output_volumes/" + str(time.strftime("%I:%M:%S_%d-%m-%Y")) + ".txt"
    else:
        dir_path = "/home/deepliver/ibrahim/dataset/100235663/100235663"
        save_path = "/home/deepliver/ibrahim/dataset/100235663/100235663_mat"
        img_path = "/home/deepliver/ibrahim/dataset/100235663/100235663_label"
        vision_path = "/home/deepliver/ibrahim/dataset/100235663/100235663_vision"
        txt_path = "/home/deepliver/ibrahim/dataset/100235663/100235663.txt"

    my_nrrd_convert = nrrd_convert.nrrd_convert()
    my_nrrd_convert.force_mkdir(save_path)
    my_nrrd_convert.force_mkdir(img_path)
    my_nrrd_convert.force_mkdir(vision_path)
    my_nrrd_convert.nrrd_image2mat(origin_dir=dir_path, vision_dir=vision_path, save_dir=save_path,
                                   image_dir=img_path, txt_dir=txt_path)


