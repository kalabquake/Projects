import serial
import serial.tools.list_ports
import time

# Get a list of available serial ports
ports = list(serial.tools.list_ports.comports())

# Print the available ports
print("Available serial ports:")
for i, port in enumerate(ports):
    print(f"{i+1}. {port.device}")

# Prompt the user to select a port
selected_port = input("Select a port to connect to: ")

# Connect to the selected port
ser = serial.Serial(ports[int(selected_port)-1].device, baudrate = 115200)


#ser.write(b"LCD.fill(65535)\r")
s=b''
s+=b"LCD.fill(65535)\n"
lines=[]
with open("binary.txt","r") as f:
    lines=f.read().split("\n")

for i in range(0,len(lines[0]),107):
    scanLine=lines[138][i:i+107]
    #print(scanLine)
    scanLine=(scanLine.replace(" ","0 ").replace("1","65535 ")).split()
    for x in range(len(scanLine)):
        scanLine[x]=int(scanLine[x])
    sendStr = "putPixelsX("+str(int(i/107))+","+str(scanLine)+")\n"
    sendStr = sendStr.encode()
    #ser.write(sendStr)
    s+=sendStr
    print(int(i/107))
    #time.sleep(1)
    #ser.write(b"LCD.lcd_show()\r")
s+=b"LCD.lcd_show()\r"

ser.write(s)
print("done")
ser.close()
