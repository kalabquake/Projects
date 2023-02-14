#frame 138
from PIL import Image

a=0
s=""
while a<9717:
  print(a)
  # Open the image file
  image = Image.open("frame"+str(a)+".jpg")

  # Get the image width and height
  width, height = image.size

  # Create a variable to store the number
  number = 0

  # Iterate over the pixels in the image
  for y in range(height):
      for x in range(width):
          # Get the pixel value
          pixel = image.getpixel((x, y))
          if("tuple" in str(type(pixel))):
              pixel=pixel[0]
          # Check if the pixel value is greater than 127
          if pixel > 127:
              # If it is, set the corresponding bit in the number
              number += 2**(x + y*width)

  # Print the final number
  l=107*80
  b=bin(number)
  b=b[2:]
  b=" "*(l-len(b))+b
  print("len:",len(b))
  b=b.replace('0',' ')
  b=b[::-1]
  

  s+=b+"\n"
  a+=1
  #print(b)
  #if(a>400):
  #  break

with open("binary.txt","w") as f:
  f.write(s)
