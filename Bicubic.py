# -*- coding: utf-8 -*-
"""
Created on Fri May 11 14:39:14 2018

@author: ASUS
"""

from PIL import Image

perbesaran = [2,4,8,10]

def langrangeInterpolation(x,x0,x1,x2,x3,fx0,fx1,fx2,fx3):
    fx = ((((x-x1)*(x-x2)*(x-x3))/((x0-x1)*(x0-x2)*(x0-x3))) *fx0) + ((((x-x0)*(x-x2)*(x-x3))/((x1-x0)*(x1-x2)*(x1-x3))) *fx1) + ((((x-x1)*(x-x0)*(x-x3))/((x2-x1)*(x2-x0)*(x2-x3))) *fx2) + ((((x-x1)*(x-x2)*(x-x0))/((x3-x1)*(x3-x2)*(x3-x0))) *fx3)
    
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
            if(j<m+1) :
                r0,g0,b0 = pixels[i,j-1]
                r1,g1,b1 = pixels[i,j-1]
                r2,g2,b2 = pixels[i,j+(m-1)]
                r3,g3,b3 = pixels[i,j+((2*m)-1)]
                
                for k in range(0,m-1,1):
                    r = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,r0,r1,r2,r3))
                    g = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,g0,g1,g2,g3))
                    b = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,b0,b1,b2,b3))
                
                    pixels[i,j+k] = (r,g,b)
                    
                
            elif(j>img.size[1]-((m*2)-1)):
                r0,g0,b0 = pixels[i,j-(m+1)]
                r1,g1,b1 = pixels[i,j-1]
                r2,g2,b2 = pixels[i,j+(m-1)]
                r3,g3,b3 = pixels[i,j+(m-1)]
                
                for k in range(0,m-1,1):
                    r = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,r0,r1,r2,r3))
                    g = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,g0,g1,g2,g3))
                    b = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,b0,b1,b2,b3))
                
                    pixels[i,j+k] = (r,g,b)
                
 
            else :
                r0,g0,b0 = pixels[i,j-(m+1)]
                r1,g1,b1 = pixels[i,j-1]
                r2,g2,b2 = pixels[i,j+(m-1)]
                r3,g3,b3 = pixels[i,j+((2*m)-1)]
                
                for k in range(0,m-1,1):
                    r = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,r0,r1,r2,r3))
                    g = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,g0,g1,g2,g3))
                    b = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,b0,b1,b2,b3))
                
                    pixels[i,j+k] = (r,g,b)
    
    return img   


def fillHorizontal(img):
    pixels = img.load()
    
    for i in range(1,img.size[0],m):
        for j in range(0,img.size[1],1):
            if(i<m+1) :
                r0,g0,b0 = pixels[i-1,j]
                r1,g1,b1 = pixels[i-1,j]
                r2,g2,b2 = pixels[i+(m-1),j]
                r3,g3,b3 = pixels[i+((2*m)-1),j]
                
                for k in range(0,m-1,1):
                    r = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,r0,r1,r2,r3))
                    g = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,g0,g1,g2,g3))
                    b = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,b0,b1,b2,b3))
                
                    pixels[i+k,j] = (r,g,b)
                
                
            elif(i>img.size[0]-((m*2)-1)):
                r0,g0,b0 = pixels[i-(m+1),j]
                r1,g1,b1 = pixels[i-1,j]
                r2,g2,b2 = pixels[i+(m-1),j]
                r3,g3,b3 = pixels[i+(m-1),j]
                
                for k in range(0,m-1,1):
                    r = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,r0,r1,r2,r3))
                    g = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,g0,g1,g2,g3))
                    b = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,b0,b1,b2,b3))
                
                    pixels[i+k,j] = (r,g,b)
                
 
            else :
                r0,g0,b0 = pixels[i-(m+1),j]
                r1,g1,b1 = pixels[i-1,j]
                r2,g2,b2 = pixels[i+(m-1),j]
                r3,g3,b3 = pixels[i+((2*m)-1),j]
                
                for k in range(0,m-1,1):
                    r = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,r0,r1,r2,r3))
                    g = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,g0,g1,g2,g3))
                    b = int(langrangeInterpolation(m+1+k,0,m,m*2,m*3,b0,b1,b2,b3))
                
                    pixels[i+k,j] = (r,g,b)
    
    return img 


if __name__ == "__main__":
    for p in perbesaran:
        m = p
        images = ["lenna x" + str(m) +".jpg", "pixel x" + str(m) +".jpg", "pixel-art x" + str(m) +".jpg", "shadow x" + str(m) +".jpg", "street-sign x" + str(m) +".jpg"]

        for image in images:
            print("processing " + image)
            image_format = image[-4::]
            filename = r"Bicubic/result_bicubic " + image + " x" + str(m) + image_format
            img = Image.open(image)
            result = resize(img)
            #result.save("resized.jpg")
            result = fillVertical(result)
            #result.save("HorizontalFilled.jpg")
            result = fillHorizontal(result)
            result.save(filename)
        
    
        
    