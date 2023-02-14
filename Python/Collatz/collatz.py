import math
import psutil

a=1

li=[a]

def checkTwo(a):
    b=int(math.log(a,2))
    return int(math.pow(2,b))==a

def collatz(a,li):
    print(a)
    print()
    
    if(a==1 or a in li):
        return
    if(a%2==0):
        if(checkTwo(a)):
            print("hit something with a factor of two")
            return
        collatz(int(a/2),li)
    else:
        collatz(int((a*3)+1),li)
    if(a not in li):
        li+=[a]

while a<40:
    print("starting:")
    collatz(a,li)
    if(a%1000==0):
        print('RAM memory % used:', psutil.virtual_memory()[2])
    print('')
    a+=1
