import math
import sys
import time

conversion=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'," ")
a=int(input("Enter number:\n"))

def run(a):
        s=""
        while a >0:
                s+=conversion[a%len(conversion)]    
                a=a//len(conversion)
        return s

#run(a)

num=10
while num<1000000000:
        t=time.time()
        a=0
        arr=[]
        while a<num:
              arr+=[run(a)]
              a+=1
        print(str(len(arr))+" in "+str(time.time()-t))
        num*=10
