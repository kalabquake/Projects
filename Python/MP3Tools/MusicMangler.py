import sys
import os
import random
droppedFiles=sys.argv
droppedFiles.remove(droppedFiles[0])
print(droppedFiles)
if(len(droppedFiles)>1):
    lib=[]
    lib1=[]
    rand=random.randrange(-254,255)
    with open(droppedFiles[0],"rb") as f:
        bytes1=f.read(1)
        count=0
        array=[]
        while len(bytes1)>0:
            lib+=[bytes1]
            bytes1=f.read(1)
            count+=1
        print("done collecting 1")
        print(len(lib))
    with open(droppedFiles[1],"rb") as f:
        bytes1=f.read(1)
        count=0
        array=[]
        while len(bytes1)>0:
            lib1+=[bytes1]
            bytes1=f.read(1)
            count+=1
        print("done collecting 2")
    count=0
    libra=[]
    while(count<len(lib) and count<len(lib1)):
        if(count>0000 and count<int(((len(lib)+len(lib1))/2)*0.8)):
            rand=random.randrange(0,100)
            if(rand%2==0):
                libra+=[lib1[count]]
            else:
                libra+=[lib[count]]
        else:
            libra+=[lib[count]]
        count+=1
    with open("Output.mp3","wb") as f:
        for a in libra:
            f.write(a)
            
    print("done")
else:
    print("You need to drop 2 files on here")
input()