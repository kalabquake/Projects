import sys
import datetime
import imageio
import PIL
from PIL import Image
import os
VALID_EXTENSIONS = ('png', 'jpg')

#sys.argv.append('CB0.png')
#sys.argv.append('CB100.png')
#sys.argv.append('CB200.png')

def create_gif(filenames):
    images = []
    output_file=input('Enter name: ')
    output_file+=".gif"
    Percent = int(input("Enter percent for image size[30 would be 30% the size of the pictures]: "))
    Percent /=100#change percent to float
    duration=float(input('Enter seconds per frame: '))
    for filename in filenames:
        img = Image.open(filename)
        img=img.resize((int(img.size[0]*Percent),int(img.size[1]*Percent)), PIL.Image.ANTIALIAS)
        #img.save('temp.png')
        #images.append(imageio.imread("temp.png"))
        images.append(img)
    imageio.mimsave(output_file, images, duration=duration)
    #os.remove("temp.png")


if __name__ == "__main__":
    script = sys.argv.pop(0)

    if len(sys.argv) < 2:
        print('Usage: python {} <duration> <path to images separated by space>'.format(script))
        sys.exit(1)

    duration = 0.5
    filenames = sys.argv


    if not all(f.lower().endswith(VALID_EXTENSIONS) for f in filenames):
        print('Only png and jpg files allowed')
        sys.exit(1)

    create_gif(filenames)
