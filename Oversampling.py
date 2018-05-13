# -*- coding: utf-8 -*-
"""
Created on Fri May 11 14:39:14 2018

@author: ASUS
"""

from PIL import Image

def langrangeInterpolation(x,x0,x1,x2,x3,fx0,fx1,fx2,fx3):
    fx = ((((x-x1)*(x-x2)*(x-x3))/((x0-x1)*(x0-x2)*(x0-x3))) *fx0) + ((((x-x0)*(x-x2)*(x-x3))/((x1-x0)*(x1-x2)*(x1-x3))) *fx1) + ((((x-x1)*(x-x0)*(x-x3))/((x2-x1)*(x2-x0)*(x2-x3))) *fx2) + ((((x-x1)*(x-x2)*(x-x0))/((x3-x1)*(x3-x2)*(x3-x0))) *fx3)
    
    return fx


def resize(img):
    pixels = img.load()
    outputResize = Image.new(img.mode, (img.size[0]*3-2, img.size[1]*3-2))
    outputResizePixels = outputResize.load()
    for i in range(0,img.size[0]):
        for j in range(0,img.size[1]):
            outputResizePixels[i*3,j*3] = pixels[i,j]
    
    return outputResize
          
     
def fillVertical(img):
    pixels = img.load()
    
    for i in range(0,img.size[0],3):
        for j in range(1,img.size[1],3):
            if(j<4) :
                r0,g0,b0 = pixels[i,j-1]
                r1,g1,b1 = pixels[i,j-1]
                r2,g2,b2 = pixels[i,j+2]
                r3,g3,b3 = pixels[i,j+5]
                
                r = int(langrangeInterpolation(4,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(4,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(4,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i,j] = (r,g,b)
                
                r = int(langrangeInterpolation(5,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(5,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(5,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i,j+1] = (r,g,b)
                
            elif(j>img.size[1]-5):
                r0,g0,b0 = pixels[i,j-4]
                r1,g1,b1 = pixels[i,j-1]
                r2,g2,b2 = pixels[i,j+2]
                r3,g3,b3 = pixels[i,j+2]
                
                r = int(langrangeInterpolation(4,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(4,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(4,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i,j] = (r,g,b)
                
                r = int(langrangeInterpolation(5,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(5,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(5,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i,j+1] = (r,g,b)
 
            else :
                r0,g0,b0 = pixels[i,j-4]
                r1,g1,b1 = pixels[i,j-1]
                r2,g2,b2 = pixels[i,j+2]
                r3,g3,b3 = pixels[i,j+5]
                
                r = int(langrangeInterpolation(4,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(4,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(4,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i,j] = (r,g,b)
                
                r = int(langrangeInterpolation(5,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(5,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(5,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i,j+1] = (r,g,b)
    
    return img   


def fillHorizontal(img):
    pixels = img.load()
    
    for i in range(1,img.size[0],3):
        for j in range(0,img.size[1],1):
            if(i<4) :
                r0,g0,b0 = pixels[i-1,j]
                r1,g1,b1 = pixels[i-1,j]
                r2,g2,b2 = pixels[i+2,j]
                r3,g3,b3 = pixels[i+5,j]
                
                r = int(langrangeInterpolation(4,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(4,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(4,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i,j] = (r,g,b)
                
                r = int(langrangeInterpolation(5,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(5,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(5,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i+1,j] = (r,g,b)
                
            elif(i>img.size[0]-5):
                r0,g0,b0 = pixels[i-4,j]
                r1,g1,b1 = pixels[i-1,j]
                r2,g2,b2 = pixels[i+2,j]
                r3,g3,b3 = pixels[i+2,j]
                
                r = int(langrangeInterpolation(4,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(4,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(4,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i,j] = (r,g,b)
                
                r = int(langrangeInterpolation(5,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(5,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(5,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i+1,j] = (r,g,b)
 
            else :
                r0,g0,b0 = pixels[i-4,j]
                r1,g1,b1 = pixels[i-1,j]
                r2,g2,b2 = pixels[i+2,j]
                r3,g3,b3 = pixels[i+5,j]
                
                r = int(langrangeInterpolation(4,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(4,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(4,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i,j] = (r,g,b)
                
                r = int(langrangeInterpolation(5,0,3,6,9,r0,r1,r2,r3))
                g = int(langrangeInterpolation(5,0,3,6,9,g0,g1,g2,g3))
                b = int(langrangeInterpolation(5,0,3,6,9,b0,b1,b2,b3))
                
                pixels[i+1,j] = (r,g,b)
    
    return img 


if __name__ == "__main__":
    img = Image.open('pixel.jpg')
    result = resize(img)
    result.save("resized.bmp")
    result = fillVertical(result)
    result.save("HorizontalFilled.bmp")
    result = fillHorizontal(result)
    result.save("result.bmp")