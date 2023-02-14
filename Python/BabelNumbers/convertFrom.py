import math
import sys


conversion=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ',',','.','!','?','&','*','(',')','-','_','+','=','[',']','#','/','\'','"')
a=int(input("Enter number:\n"))

s=""
while a >0:
        s+=conversion[a%len(conversion)]    
        a=a//len(conversion)

print(s)
