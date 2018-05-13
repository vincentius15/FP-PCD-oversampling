# -*- coding: utf-8 -*-
"""
Created on Sun May 13 11:47:53 2018

@author: ASUS
"""

from skimage import data, img_as_float, io
from skimage.measure import compare_ssim as ssim

img = img_as_float(io.imread("facet.jpg"))

ssim_none = ssim(img, img, data_range=img.max() - img.min(), multichannel=True)

print(ssim_none)