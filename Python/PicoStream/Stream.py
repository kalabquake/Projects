import serial
import serial.tools.list_ports
import sys
import threading
import keyboard
import time
import pyscreenshot

p=None
s=None

def convert(red,green,blue):
    #r=(int((red/255)*63))<<5
    #g=(int((green/255)*31))
    #b=(int((blue/255)*31))<<11
    #print(r|g|b)
    b=(int((blue/255)*31)&0x1F)<<8
    r=(int((red/255)*31)&0x1F)<<3
    g=(int((green/255)*7)&0x07)
    return r|g|b


def selectPort():
    global p
    ports=[]
    print("Available ports:")
    for port in serial.tools.list_ports.comports():
            print(port.name)
            ports+=[port.name]
    print("")
    if(len(ports)==0):
            input("no ports found...\n<press enter to exit>")
            sys.exit()

    while p not in ports:
            p=input("Enter port: ")
            if p not in ports:
                    print("Error: invalid port")

def printSerial():
    global s
    st=b''
    while(not keyboard.is_pressed('esc')):
        if(s.inWaiting()>0):
            b=s.read()
            st+=b
            print(str(b)[2:len(b)+2],end='')
            if(b==b'\n'):
                print("")
            st=b''
selectPort()
s = serial.Serial(port=p,baudrate=115200,timeout=1,parity=serial.PARITY_EVEN,rtscts=1)
t1 = threading.Thread(target=printSerial)
t1.start()

#s.write(b'putPixel(0,0,0xFFFF)')
#s.write(b'LCD.fill(65535)\r\n')
#s.write(0)
#s.write(b'LCD.lcd_show()\r\n')
#s.write(0)

im = pyscreenshot.grab()
im = im.resize((240,135))
width,height=im.size
pixels=im.load

s.write(b'LCD.fill(65535)\r\n')
s.write(0)
p=[0 for j in range(height)]

for x in range(width):
    for y in range(height):
        #if(keyboard.is_pressed('esc')):
        #   s.close()
        #   print("closed early")
        #   sys.exit()
        r,g,b=im.getpixel((x,y))
        rgb=0#convert(r,g,b)
        p[y]=rgb
        #putPixel(x,y,color)
        st='putPixel('+str(y)+','+str(x)+','+str(rgb)+')\r\n'
        s.write(bytes(st, 'utf-8'))
        s.write(0)
        #time.sleep(0.001)
        #s.write(b'LCD.lcd_show()\r\n')
        #s.write(0)
    #print("made array!")
    #s.write(bytes(str("putPixels("+str(x)+","+str(p)+")"), 'utf-8')+b"\r\n")
    #s.write(0)
    #time.sleep(2)
    p=[0 for j in range(height)]
    if(x%50==0):
        s.write(b'LCD.lcd_show()\r\n')
        s.write(0)
    if(x>=255):
        break#seems like the screen is a few pixels shorter than I thought


s.write(b'LCD.lcd_show()\r\n')
s.write(0)
t1.join()
print("Done")
s.close()
#def putPixel(x,y,color):
#    LCD.hline(y,x,1,color)
