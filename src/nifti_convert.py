#!/usr/bin/env python
#  -*- coding: utf-8 -*

from __future__ import print_function

import os
import scipy.io as scio
import numpy as np
import shutil
from PIL import Image
from nifti import *


class nifti_convert(object):
    def __init__(self):
        self.nifti_image = set(['nii'])
        self.nifti_label = set(['label.nii'])

    def MatrixToImage(self, data):
        new_im = Image.fromarray(data.astype(np.uint8))
        return new_im

    def nii_image2mat(self, dir, save_dir, image_dir):
        nim = NiftiImage(dir)
        rows, cols, ths = nim.extent
        print('root:', dir, 'ths:', ths)

        volume = np.zeros((ths, 512, 512), dtype=np.float32)
        for i in range(ths):
            nim = NiftiImage(dir)
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

