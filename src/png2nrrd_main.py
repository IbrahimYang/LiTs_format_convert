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

import nrrd_convert
import os
import shutil

if __name__ == '__main__':
    input_dir = "/home/ibrahim/Desktop/50"
    savepath = "/home/ibrahim/Desktop"

    # if os.path.exists(savepath):
    #     shutil.rmtree(savepath)
    # os.makedirs(savepath)

    my_nrrd_convert = nrrd_convert.nrrd_convert()
    my_nrrd_convert.bmp2nrrd(origin_dir=input_dir, nrrd_dir=savepath)
    # for i in range(0, 1):
    #     dir_now = input_dir + str(i)
    #     my_nrrd_convert.bmp2nrrd(origin_dir=input_dir, nrrd_dir=savepath)



