# -*- coding: utf-8 -*-
"""
Created on Fri May 11 14:39:14 2018

@author: ASUS
"""

from PIL import Image

perbesaran = [2,4,8,10]

def langrangeInterpolation(x,x0,x1,fx0,fx1):
    fx = ((((x-x1))/((x0-x1))) *fx0) + ((((x-x0))/((x1-x0))) *fx1)
    
    return fx


def resize(img):
    pixels = img.load()
    outputResize = Image.new(img.mode, (img.size[0]*m-(m-1), img.size[1]*m-(m-1)))
    outputResizePixels = outputResize.load()
    for i in range(0,img.size[0]):
        for j in range(0,img.size[1]):
            outputResizePixels[i*m,j*m] = pixels[i,j]
    
    return outputResize
          
     
def fillVertical(img):
    pixels = img.load()
    
    for i in range(0,img.size[0],m):
        for j in range(1,img.size[1],m):
            r0,g0,b0 = pixels[i,j-1]
            r1,g1,b1 = pixels[i,j+(m-1)]
            
            for k in range(0,m-1,1):
                r = int(langrangeInterpolation(1+k,0,m,r0,r1))
                g = int(langrangeInterpolation(1+k,0,m,g0,g1))
                b = int(langrangeInterpolation(1+k,0,m,b0,b1))
                
                pixels[i,j+k] = (r,g,b)
    
    return img   


def fillHorizontal(img):
    pixels = img.load()
    
    for i in range(1,img.size[0],m):
        for j in range(0,img.size[1],1):
            r0,g0,b0 = pixels[i-1,j]
            r1,g1,b1 = pixels[i+(m-1),j]
            
            for k in range(0,m-1,1):
                r = int(langrangeInterpolation(1+k,0,m,r0,r1))
                g = int(langrangeInterpolation(1+k,0,m,g0,g1))
                b = int(langrangeInterpolation(1+k,0,m,b0,b1))
            
                pixels[i+k,j] = (r,g,b)
    
    return img 


if __name__ == "__main__":
    for p in perbesaran:
        m = p
        images = ["lenna x" + str(m) +".jpg", "pixel x" + str(m) +".jpg", "pixel-art x" + str(m) +".jpg", "shadow x" + str(m) +".jpg", "street-sign x" + str(m) +".jpg"]

        for image in images:
            print("processing " + image)
            image_format = image[-4::]
            filename = r"Bilinear/result_bilinear " + image + " x" + str(m) + image_format
            img = Image.open(image)
            result = resize(img)
            #result.save("resized.jpg")
            result = fillVertical(result)
            #result.save("HorizontalFilled.jpg")
            result = fillHorizontal(result)
            result.save(filename)