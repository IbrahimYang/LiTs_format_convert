"""
*****************************************************************************
*******************Ibrahim,CBICR,Tsinghua University*************************
*****************************************************************************
File name:    nrrd_convert.py
Description:  convert .nrrd format image and label to .png or .mat
Author:       Ibrahim Yang
Version:      V1.0
Date:         2018-11-6
History:
*****************************************************************************
"""
from __future__ import print_function

import os
import scipy.io as scio
import numpy as np
import shutil
from PIL import Image
from nifti import *


class nifti_convert(object):
    """
    Function:
        nii convert class
    Parameters:
      dir, save_dir, vision_dir,image_dir
    Returns:
      .png or .mat images
    """
    def __init__(self):
        self.nifti_image = set(['nii'])
        self.nifti_label = set(['label.nii'])

    def MatrixToImage(self, data):
        """
        Function:
            MatrixToImage
        Parameters:
          data: numpy image data
        Returns:
          PIL format image
        """
        new_im = Image.fromarray(data.astype(np.uint8))
        return new_im

    def nii_image2mat(self, origin_dir, save_dir, image_dir):
        """
        Function:
            nii_image2mat
        Parameters:
          origin_dir: origin path
          save_dir: save .mat format image
          image_dir: save .png format label
        Returns:
          save .mat format image in save_dir
        """
        nim = NiftiImage(origin_dir)
        rows, cols, ths = nim.extent
        print('root:', origin_dir, 'ths:', ths)

        volume = np.zeros((ths, 512, 512), dtype=np.float32)
        for i in range(ths):
            nim = NiftiImage(origin_dir)
            volume[i, :, :] = nim.data[i]

        for w in range(ths):
            for x in range(rows):
                for y in range(cols):
                    if volume[w, x, y] < -150:
                        volume[w, x, y] = -150
                    elif volume[w, x, y] > 250:
                        volume[w, x, y] = 250

        min_nii_data = np.min(volume)
        max_nii_data = np.max(volume)
        print('min_nii_data:', min_nii_data)
        print('max_nii_data:', max_nii_data)

        for j in range(ths):
            data_Normalization = 255.0 * (volume[j, :, :] - min_nii_data) / (max_nii_data - min_nii_data)
            scio.savemat((save_dir + "/" + str(j + 1) + ".mat"), {'section': data_Normalization})
            new_im = self.MatrixToImage(data_Normalization)
            new_im.save(image_dir + '/' + str(j) + '.bmp')
            print('output:', j)

