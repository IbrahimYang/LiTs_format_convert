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
import nrrd
import scipy.io as scio
import numpy as np
from PIL import Image

class nrrd_convert(object):
    """
    Function:
        nrrd convert class
    Parameters:
      dir, save_dir, vision_dir,image_dir
    Returns:
      .png or .mat images
    """
    def __init__(self):
        self.nrrd_image = 'nrrd'
        self.nrrd_label = 'label.nrrd'
        self.bmp_image = 'bmp'
        self.png_image = 'png'

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

    def clean_mkdir(self, path):
        """
        Function:
            clean_mkdir
        Parameters:
          path: input the path need to clean
        Returns:
          PIL format image
        """
        if os.path.exists(path) == 0:
            os.makedirs(path)
            print('creat_path:', path)

    def nrrd_image2mat(self, origin_dir, save_dir, vision_dir, image_dir, txt_dir):
        """
        Function:
            nrrd_image2mat
        Parameters:
          origin_dir: origin path
          save_dir: save .mat format image
          vision_dir: save .bmp format image
          image_dir: save .png format label
          txt_dir: save inference txt
        Returns:
          save .mat format image in save_dir
          save .bmp format image in vision_dir
          save .bmp format label in image_dir
          save .txt format inference adress in txt_dir
        """
        if os.path.exists(txt_dir):
            os.remove(txt_dir)
        inference_adress = file(txt_dir, "a+")
        for root, dirs, files in os.walk(origin_dir):
            for single_file in files:
                apath = os.path.join(root, single_file)

                image_dir_now = image_dir + '/' + str(root.split('/')[-1])
                save_dir_now = save_dir + '/' + str(root.split('/')[-1])
                vision_dir_now = vision_dir + '/' + str(root.split('/')[-1])

                self.clean_mkdir(save_dir_now)
                self.clean_mkdir(image_dir_now)
                self.clean_mkdir(vision_dir_now)

                if apath.split('.')[-1] in self.nrrd_image:
                    if apath.split('-')[-1] in self.nrrd_label:
                        single_data, ops = nrrd.read(apath)
                        rows, cols, ths = single_data.shape
                        print('root:', apath, 'ths:', ths)

                        single_data = single_data[::-1, :, :]
                        single_data = single_data[:, ::-1, :]

                        min_nrrd_data = np.min(single_data)
                        max_nrrd_data = np.max(single_data)
                        print('min_nrrd_data:', min_nrrd_data)
                        print('max_nrrd_data:', max_nrrd_data)

                        for j in range(ths):
                            data_Normalization = 255.0 * (single_data[:, :, j] - min_nrrd_data) / (
                                    max_nrrd_data - min_nrrd_data)
                            new_im = self.MatrixToImage(data_Normalization)
                            new_im.save(image_dir_now + '/' + str(j+1) + '.png')
                            print('output:', j)
                    else:
                        single_data, ops = nrrd.read(apath)
                        rows, cols, ths = single_data.shape
                        print('root:', apath, 'ths:', ths)

                        for adress_counter in range(ths - 2):
                            inference_adress.write('images_volumes/' + str(root.split('/')[-1]) + "/" +
                                                   str(adress_counter + 1) + ".mat" + " ")
                            inference_adress.write('item_seg/' + str(root.split('/')[-1]) + "/" +
                                                   str(adress_counter + 1) + ".png" + " ")
                            inference_adress.write('liver_seg/' + str(root.split('/')[-1]) + "/" +
                                                   str(adress_counter + 1) + ".png" + " ")

                            inference_adress.write('images_volumes/' + str(root.split('/')[-1]) + "/" +
                                                   str(adress_counter + 2) + ".mat" + " ")
                            inference_adress.write('item_seg/' + str(root.split('/')[-1]) + "/" +
                                                   str(adress_counter + 2) + ".png" + " ")
                            inference_adress.write('liver_seg/' + str(root.split('/')[-1]) + "/" +
                                                   str(adress_counter + 2) + ".png" + " ")

                            inference_adress.write('images_volumes/' + str(root.split('/')[-1]) + "/" +
                                                   str(adress_counter + 3) + ".mat" + " ")
                            inference_adress.write('item_seg/' + str(root.split('/')[-1]) + "/" +
                                                   str(adress_counter + 3) + ".png" + " ")
                            inference_adress.write('liver_seg/' + str(root.split('/')[-1]) + "/" +
                                                   str(adress_counter + 3) + ".png" + " ")
                            inference_adress.write(str(0.000048) + str(0.011301) + "\n")

                        for w in range(ths):
                            for x in range(rows):
                                for y in range(cols):
                                    if single_data[x, y, w] < -150:
                                        single_data[x, y, w] = -150
                                    elif single_data[x, y, w] > 250:
                                        single_data[x, y, w] = 250

                        min_nrrd_data = np.min(single_data)
                        max_nrrd_data = np.max(single_data)
                        print('min_nrrd_data:', min_nrrd_data)
                        print('max_nrrd_data:', max_nrrd_data)

                        single_data = single_data[::-1, :, :]
                        single_data = single_data[:, ::-1, :]

                        for j in range(ths):
                            data_Normalization = 255.0 * (single_data[:, :, j] - min_nrrd_data) / (
                                    max_nrrd_data - min_nrrd_data)
                            scio.savemat((save_dir_now + "/" + str(j+1) + ".mat"), {'section': data_Normalization})
                            new_im = self.MatrixToImage(data_Normalization)
                            new_im.save(vision_dir_now + '/' + str(j+1) + '.png')
                            print('output:', j)
        inference_adress.close()

    def nrrd_label2bmp(self, origin_dir, image_dir):
        """
        Function:
            only convert nrrd label
        Parameters:
          origin_dir: origin path
          image_dir: save .png format label
        Returns:
          save .bmp format label in image_dir
        """
        for root, dirs, files in os.walk(origin_dir):
            for single_file in files:
                apath = os.path.join(root, single_file)
                if apath.split('.')[-1] in self.nrrd_image:
                    if apath.split('-')[-1] in self.nrrd_label:
                        single_data, ops = nrrd.read(apath)
                        rows, cols, ths = single_data.shape
                        print('root:', apath, 'ths:', ths)

                        single_data = single_data[::-1, :, :]
                        single_data = single_data[:, ::-1, :]

                        min_nrrd_data = np.min(single_data)
                        max_nrrd_data = np.max(single_data)
                        print('min_nrrd_data:', min_nrrd_data)
                        print('max_nrrd_data:', max_nrrd_data)

                        for j in range(ths):
                            data_Normalization = 255.0 * (single_data[:, :, j] - min_nrrd_data) / (
                                    max_nrrd_data - min_nrrd_data)
                            new_im = self.MatrixToImage(data_Normalization)
                            new_im.save(image_dir + '/' + str(j) + '.bmp')
                            print('output:', j)
                    else:
                        pass

    def bmp2nrrd(self, origin_dir, nrrd_dir):
        """
        Function:
            only convert nrrd label
        Parameters:
          origin_dir: origin .png or .bmp path
          nrrd_dir: save .nrrd format label
        Returns:
          save .nrrd format in nrrd_dir
        """
        dirpath = "./7 Abdomen_V  1.5  B31f_2.nrrd"
        real_header = nrrd.read_header(dirpath)    #read header

        for root, dirs, files in os.walk(origin_dir):
            files = sorted(files, key=lambda x: int(x.split('.')[0]))
            first_path = os.path.join(root, files[0])
            first_image = np.array(Image.open(first_path))
            nrrd_numpy = np.zeros((np.shape(first_image)[0], np.shape(first_image)[1], len(files)))
            filename = nrrd_dir + '/' + str(root.split('/')[-1]) + '.nrrd'
            print(nrrd_numpy.shape)
            for i, single_file in enumerate(files):
                apath = os.path.join(root, single_file)
                if apath.split('.')[-1] in self.png_image:       #png iamge
                    image = np.array(Image.open(apath))
                    nrrd_numpy[:, :, i] = image
                elif apath.split('.')[-1] in self.bmp_image:      #bmp iamge
                    image = np.array(Image.open(apath))
                    nrrd_numpy[:, :, i] = image
                else:
                    pass
            nrrd.write(filename, nrrd_numpy, real_header)
            # single_data, ops = nrrd.read(filename)
            # print(single_data)
            # print(ops)
