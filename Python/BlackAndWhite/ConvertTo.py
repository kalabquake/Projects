from PIL import Image
import sys

sys.argv.append('rainbow.jpg')

if(len(sys.argv)<2):
    input("Drop an image onto this script\n<press enter to exit>")
    sys.exit()

img=Image.open(sys.argv[1])
newimg=Image.new(img.mode,img.size)

i=img.load()
ni=newimg.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        b=int(0.3*i[x,y][0])+int(0.59*i[x,y][1])+int(0.11*i[x,y][2])
        ni[x,y]=(b,b,b)
        
newimg.show()
