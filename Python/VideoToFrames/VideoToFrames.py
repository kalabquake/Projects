import cv2
vidcap = cv2.VideoCapture('badAppleCropped.mp4')
success,image = vidcap.read()
count = 0
while success:
  image=cv2.resize(image,(107,80),interpolation=cv2.INTER_AREA)
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
  #if(count>138):
  #  break
