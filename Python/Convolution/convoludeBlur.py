from PIL import Image
import numpy as np

img = Image.open("example.png")
#pixels=img.load()

width,height=img.size
newImg= Image.new(mode='RGB',size=(width,height))
newPixels=newImg.load()

n=int(input("convolution size: "))

cs=[]
for i in range(width):
    for j in range(height):
        c=img.getpixel((i,j))
        if(len(c)==1):
            #do stuff for black and white
            #print("not made yet")
            greys=[[0 for b in range(n)] for a in range(n)]
        else:
            #do stuff for color image
            #cs=[[() for b in range(n)] for a in range(n)]
            reds=[[0 for b in range(n)] for a in range(n)]
            greens=[[0 for b in range(n)] for a in range(n)]
            blues=[[0 for b in range(n)] for a in range(n)]
            k=0
            l=0
            for x in range(i-(n//2),i+(n//2)):
                for y in range(j-(n//2),j+(n//2)):
                    #cs[k][l]=img.getpixel((i,j))
                    if(x>=0 and x<width and y>=0 and y<height):
                        
                        c=img.getpixel((x,y))
                    else:
                        c=(0,0,0)#out of bounds is just considered black
                    #print(x,y)
                    reds[k][l]=c[0]
                    greens[k][l]=c[1]
                    blues[k][l]=c[2]
                    l+=1
                l=0
                k+=1

            r=0
            for x in reds:
                for y in x:
                    r+=int((1/(n*n))*y)
            if(r<0):
                r=0
            else:
                r%=255
            g=0
            for x in greens:
                for y in x:
                    g+=int((1/(n*n))*y)
            if(g<0):
                g=0
            else:
                g%=255
            b=0
            for x in blues:
                for y in x:
                    b+=int((1/(n*n))*y)
            if(b<0):
                b=0
            else:
                b%=255
            newPixels[i,j]=(r,g,b)
            
newImg.show()
