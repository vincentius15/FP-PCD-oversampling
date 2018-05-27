# -*- coding: utf-8 -*-
"""
Created on Fri May 11 14:39:14 2018

@author: ASUS
"""

from PIL import Image

perbesaran = [2,4,8,10]

def resize(img):
    pixels = img.load()
    outputResize = Image.new(img.mode, (img.size[0]*m, img.size[1]*m))
    outputResizePixels = outputResize.load()
    for i in range(0,img.size[0]):
        for j in range(0,img.size[1]):
            outputResizePixels[i*m,j*m] = pixels[i,j]
    
    return outputResize
          
     
def fillVertical(img):
    pixels = img.load()
    
    for i in range(0,img.size[0],m):
        for j in range(0,img.size[1],m):
            r0,g0,b0 = pixels[i,j]
            for k in range(1,m,1):
                pixels[i,j+k] = (r0,g0,b0)
    
    return img   

def fillHorizontal(img):
    pixels = img.load()
    
    for i in range(0,img.size[0],m):
        for j in range(0,img.size[1],1):
            r0,g0,b0 = pixels[i,j]
            for k in range(1,m,1):
                pixels[i+k,j] = (r0,g0,b0)
    
    return img 

if __name__ == "__main__":
    for p in perbesaran:
        m = p
        images = ["lenna x" + str(m) +".jpg", "pixel x" + str(m) +".jpg", "pixel-art x" + str(m) +".jpg", "shadow x" + str(m) +".jpg", "street-sign x" + str(m) +".jpg"]

        for image in images:
            print("processing " + image)
            image_format = image[-4::]
            filename = r"Nearest neighbor/result_nearestneighbor " + image + " x" + str(m) + image_format
            img = Image.open(image)
            result = resize(img)
            #result.save("resized.jpg")
            result = fillVertical(result)
            #result.save("HorizontalFilled.jpg")
            result = fillHorizontal(result)
            result.save(filename)