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
    standard_adress = 1
    if standard_adress:
        input_dir = "../liver_database/4-input_result_th"
        save_dir = "../liver_database/5-output_nrrd"
        template_path = "../data_template/7 Abdomen_V  1.5  B31f_2.nrrd"
    else:
        input_dir = "/home/ibrahim/Desktop/th_test"
        save_dir = "/home/ibrahim/Desktop/th_test_out"
        template_path = "/home/ibrahim/PycharmProjects/LiTs_format_convert/data_template/7 Abdomen_V  1.5  B31f_2.nrrd"

    my_nrrd_convert = nrrd_convert.nrrd_convert()
    my_nrrd_convert.force_mkdir(save_dir)
    my_nrrd_convert.bmp2nrrd(origin_dir=input_dir, template_dir=template_path, nrrd_dir=save_dir)


