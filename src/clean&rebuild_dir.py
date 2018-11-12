"""
*****************************************************************************
*******************Ibrahim,CBICR,Tsinghua University*************************
*****************************************************************************
File name:    clean&rebuild_dir.py
Description:  clean&rebuild liver_database dir
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
    liver_database_path = "../liver_database"

    my_nrrd_convert = nrrd_convert.nrrd_convert()
    my_nrrd_convert.force_mkdir(liver_database_path + "/1-input_nrrd")
    my_nrrd_convert.force_mkdir(liver_database_path + "/2-output_volumes")
    my_nrrd_convert.force_mkdir(liver_database_path + "/3-input_result")
    my_nrrd_convert.force_mkdir(liver_database_path + "/4-input_result_th")
    my_nrrd_convert.force_mkdir(liver_database_path + "/5-output_nrrd")




