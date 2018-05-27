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

def NeighFunc(img):
    pixels = img.load()
    output = Image.new(img.mode, (img.size[0], img.size[1]))
    outputpixels = output.load()
    for i in range(0,img.size[0],1):
        for j in range(0,img.size[1],1):
            r0,g0,b0 = pixels[i,j]
            if r0!=0 and g0!=0 and b0!=0:
                continue
            if i>0 and j>0:
                r1,g1,b1 = pixels[i-1,j-1]
                r0 = max(r0,r1)
                g0 = max(g0,g1)
                b0 = max(b0,b1)
            if i+1<img.size[0] and j>0:
                r1,g1,b1 = pixels[i+1,j-1]
                r0 = max(r0,r1)
                g0 = max(g0,g1)
                b0 = max(b0,b1)
            if i+1<img.size[0] and j+1<img.size[1]:
                r1,g1,b1 = pixels[i+1,j+1]
                r0 = max(r0,r1)
                g0 = max(g0,g1)
                b0 = max(b0,b1)
            if i>0 and j+1<img.size[1]:
                r1,g1,b1 = pixels[i-1,j+1]
                r0 = max(r0,r1)
                g0 = max(g0,g1)
                b0 = max(b0,b1)
            #eval left
            if i>0:
                r1,g1,b1 = pixels[i-1,j]
                r0 = max(r0,r1)
                g0 = max(g0,g1)
                b0 = max(b0,b1)
            #eval right
            if i+1<img.size[0]:
                r1,g1,b1 = pixels[i+1,j]
                r0 = max(r0,r1)
                g0 = max(g0,g1)
                b0 = max(b0,b1)
            #eval top
            if j>0:
                r1,g1,b1 = pixels[i,j-1]
                r0 = max(r0,r1)
                g0 = max(g0,g1)
                b0 = max(b0,b1)
            #eval bot
            if j+1<img.size[1]:
                r1,g1,b1 = pixels[i,j+1]
                r0 = max(r0,r1)
                g0 = max(g0,g1)
                b0 = max(b0,b1)
            outputpixels[i,j]=(r0,g0,b0)
    return output

if __name__ == "__main__":
    img = Image.open('facet.jpg')
    result = resize(img)
    result.save("resized.bmp")
    result2 = NeighFunc(result)
    result2.save("neigh_func.bmp")