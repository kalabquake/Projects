from PIL import Image
import numpy as np

img = Image.open("example.png")
img=img.convert('RGB')
#pixels=img.load()

width,height=img.size
newImg= Image.new(mode='RGB',size=(width,height))
newPixels=newImg.load()

n=int(input("convolution size: "))

cs=[]
for i in range(width):
    for j in range(height):
        c=img.getpixel((i,j))
        if((str(c)).isdigit()):
            #do stuff for black and white
            print("not made yet")
            greys=[[0 for b in range(n)] for a in range(n)]
            k=0
            l=0
            for x in range(i-(n//2),i+(n//2)+1):
                for y in range(j-(n//2),j+(n//2)+1):
                    #cs[k][l]=img.getpixel((i,j))
                    if(x>=0 and x<width and y>=0 and y<height):
                        #print(i,j)
                        c=img.getpixel((x,y))
                    else:
                        c=0#out of bounds is just considered black

                    greys[k][l]=c
                    l+=1
                l=0
                k+=1
            g= int(np.linalg.det(np.array(greys)))#%255
            if(g<0):
                g=0
            else:
                g%=255
            newPixels[i,j]=(g,g,g)

        else:
            #do stuff for color image
            #cs=[[() for b in range(n)] for a in range(n)]
            reds=[[0 for b in range(n)] for a in range(n)]
            greens=[[0 for b in range(n)] for a in range(n)]
            blues=[[0 for b in range(n)] for a in range(n)]
            k=0
            l=0
            for x in range(i-(n//2),i+(n//2)+1):
                for y in range(j-(n//2),j+(n//2)+1):
                    #cs[k][l]=img.getpixel((i,j))
                    if(x>=0 and x<width and y>=0 and y<height):
                        #print(i,j)
                        c=img.getpixel((x,y))
                    else:
                        c=(0,0,0)#out of bounds is just considered black

                    reds[k][l]=c[0]
                    greens[k][l]=c[1]
                    blues[k][l]=c[2]
                    l+=1
                l=0
                k+=1
                
            r= int(np.linalg.det(np.array(reds)))#%255
            if(r<0):
                r=0
            else:
                r%=255
            g= int(np.linalg.det(np.array(greens)))#%255
            if(g<0):
                g=0
            else:
                g%=255
            b= int(np.linalg.det(np.array(blues)))#%255
            if(b<0):
                b=0
            else:
                b%=255
            newPixels[i,j]=(r,g,b)
            
newImg.show()
