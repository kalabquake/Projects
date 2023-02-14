import serial
import serial.tools.list_ports
import random
import threading
import keyboard
import time

p=None
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

t1 = threading.Thread(target=printSerial)
t1.start()
#38400
s = serial.Serial(port=p,baudrate=1,timeout=1,parity=serial.PARITY_EVEN,rtscts=1)
s.write(b'LCD.fill(65535)\r\n')
s.write(0)

a=0
while(1):
    color = 0#random.randint(0,65536)
    st='LCD.fill('+str(color)+')\r\n'
    s.write(bytes(st, 'utf-8'))
    #LCD.text("Pico WIFI",60,60,LCD.red)
    st='LCD.text("'+str(a)+'",60,60,'+str(65535-color)+')\r\n'
    a+=1
    s.write(bytes(st, 'utf-8'))
    s.write(0)
    s.write(b'LCD.lcd_show()\r\n')
    s.write(0)
    time.sleep(0.05)

t1.join()
