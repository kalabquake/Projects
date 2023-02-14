from PIL import Image

def convert(red,green,blue):
    #r=(int((red/255)*63))<<5
    #g=(int((green/255)*31))
    #b=(int((blue/255)*31))<<11
    #print(r|g|b)
    b=(int((blue/255)*31)&0x1F)<<8
    r=(int((red/255)*31)&0x1F)<<3
    g=(int((green/255)*7)&0x07)
    return r|g|b

img = Image.open("./test2_2.png")
#pixels=img.load()

width,height = img.size

mwidth,mheight=(240,135)
if(width>mwidth or height>mheight):
    dif=1
    if(width>height):
        dif=width/mwidth
    else:
        dif=height/mheight
    width,height=(int(width*dif),int(height*dif))

img = img.resize((width,height))
pixels=img.load()
cpixels=[[0 for i in range(width)] for j in range(height)]

for i in range(width):
    for j in range(height):
        #r,g,b=(0,0,0)
        r,g,b = img.getpixel((i,j))
        cpixels[j][i]=convert(r,g,b)
        #break
    #break
print(cpixels)
