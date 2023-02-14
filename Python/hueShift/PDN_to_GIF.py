import sys
import datetime
import imageio
import pypdn
import PIL
from PIL import Image
import os
import substring
VALID_EXTENSIONS = ('pdn')


def create_gif(layeredImage):
    images = []
    output_file=input('Enter name: ')
    output_file+=".gif"
    Percent = int(input("Enter percent for image size[30 would be 30% the size of the pictures]: "))
    Percent /=100#change percent to float
    duration=input('Enter seconds per frame: ')
    for layer in layeredImage.layers:
        img = layer.image
        #print(img.size)
        #input("<press enter>")
        #img=img.resize(30,30,PIL.Image.ANTIALIAS)#(int(img.size[0]*Percent),int(img.size[1]*Percent)), PIL.Image.ANTIALIAS)
        img=Image.fromarray(img).resize((int(Percent*len(img)),int(Percent*len(img[0]))),PIL.Image.ANTIALIAS)
        #img.save('temp.png')
        images.append(img)
    images+=images[::-1]
    imageio.mimsave(output_file, images, duration=duration)
	#os.remove("temp.png")


if __name__ == "__main__":
	a=sys.argv.pop(1)
	print(a)
	layeredImage=pypdn.read(a)
	if not (a[-4:]=='.pdn'):
		print('Only pdn files allowed')
		sys.exit(1)
	create_gif(layeredImage)