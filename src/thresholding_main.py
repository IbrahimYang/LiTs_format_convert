"""
*****************************************************************************
*******************Ibrahim,CBICR,Tsinghua University*************************
*****************************************************************************
File name:    thresholding_main.py
Description:  threshold png or bmp image
Author:       Ibrahim Yang
Version:      V1.0
Date:         2018-11-12
History:
*****************************************************************************
"""
from __future__ import print_function

import sys
sys.path.append("..")
import nrrd_convert

"""
Function:     main
Description:  threshold png or bmp image
Calls:        nrrd_convert
Called By:    none
Input:        none
Output:       none
Return:       ./*.png
Others:       none
"""
if __name__ == '__main__':
    standard_adress = 1
    if standard_adress:
        input_dir = "../liver_database/3-input_result"
        save_dir = "../liver_database/4-input_result_th"
    else:
        input_dir = "/home/ibrahim/Desktop/th_test"
        save_dir = "/home/ibrahim/Desktop/th_test_out"

    my_nrrd_convert = nrrd_convert.nrrd_convert()
    my_nrrd_convert.force_mkdir(save_dir)
    my_nrrd_convert.thresholding(origin_dir=input_dir, save_dir=save_dir)



