import pytesseract
from PIL import ImageGrab
import sys
import subprocess
import numpy
import pyperclip

# Open Snipping Tool so you can snip the image
subprocess.Popen([r'C:\Windows\system32\SnippingTool.exe'])

input('<press enter when image is in clipboard>')
img = ImageGrab.grabclipboard()
while(img==None):
    print('No image in clipboard!')
    subprocess.Popen([r'C:\Windows\system32\SnippingTool.exe'])
    input('<press enter when image is in clipboard>')
    img = ImageGrab.grabclipboard()

print("Output:\n")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
a=pytesseract.image_to_string(numpy.array(img), config="--psm 6")
print(a)
pyperclip.copy(a)
