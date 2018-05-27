# -*- coding: utf-8 -*-
"""
Created on Sun May 13 11:47:53 2018

@author: ASUS
"""
from skimage import img_as_float, io
from skimage.measure import compare_ssim as ssim
from os import listdir

folders = ["Bicubic", "Bilinear", "Nearest neighbor"]

for folder in folders:
    images = listdir("Hasil photoshop/" + folder)
    for image in images:
        imgpath = "Hasil photoshop/" + folder + "/" + image
        img = img_as_float(io.imread(imgpath))
        
        imgname = image.split(" ")
        referencepath = "Reference/Nearest neighbor/" + imgname[0] + " " + str(img.shape[1]) + " " + str(img.shape[0])+".jpg"
        reference = img_as_float(io.imread(referencepath))

        ssim_none = ssim(img, reference, data_range=img.max() - img.min(), multichannel=True)

        print(imgpath + ";" + str(ssim_none))