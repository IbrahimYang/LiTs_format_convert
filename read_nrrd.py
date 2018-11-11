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

import nrrd
import os
import shutil
import numpy as np

if __name__ == '__main__':
    # my_nrrd_convert = nrrd_convert.nrrd_convert()

    dirpath = "/home/ibrahim/dataset/2018.9.21.yyl/186967/7 Abdomen_V  1.5  B31f_2.nrrd"
    single_data, ops = nrrd.read(dirpath)
    print(single_data)
    print(ops)
