import pypdn
from PIL import Image
from inspect import getmembers, isfunction
import colorsys
import numpy as np

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)


def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = hout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def colorize(image, hue):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.
    """
    img = image.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')

    return new_img


def printFunc(obj):
    a=[o for o in getmembers(obj) if isfunction(o[1])]
    for x in a:
        print(x[0])
	
img=pypdn.read('landscape.pdn')
i=0
while i<359:
    h=Image.fromarray(img.layers[0].image)
    h=colorize(h,i)
    h.save('R&R'+str(i)+".png")
    i+=1

print(len(img.layers))
