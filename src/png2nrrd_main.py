"""
*****************************************************************************
*******************Ibrahim,CBICR,Tsinghua University*************************
*****************************************************************************
File name:    png_nrrd_main.py
Description:  convert png or bmp to nrrd
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
Description:  convert png to nrrd image
Calls:        nrrd_convert
Called By:    none
Input:        none
Output:       none
Return:       ./*.nrrd
Others:       none
"""
if __name__ == '__main__':
    input_dir = "/home/deepliver/Desktop/seg_liver/V"
    save_dir = "/home/deepliver/Desktop/liver_seg"

    my_nrrd_convert = nrrd_convert.nrrd_convert()
    my_nrrd_convert.force_mkdir(save_dir)
    my_nrrd_convert.bmp2nrrd(origin_dir=input_dir, nrrd_dir=save_dir)

    # for i in range(0, 2):
    #     dir_now = input_dir + str(i)
    #     my_nrrd_convert.bmp2nrrd(origin_dir=dir_now, nrrd_dir=save_dir)



