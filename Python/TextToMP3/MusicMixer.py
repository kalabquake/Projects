import sys
import os
import random
droppedFiles=sys.argv
droppedFiles.remove(droppedFiles[0])
#print(droppedFiles)
if(len(droppedFiles)>1):
    libs=[[] for y in range(len(droppedFiles))]
    count=0
    avg=0
    while count < len(droppedFiles):
        #print(droppedFiles[count])
        with open(droppedFiles[count],"rb") as f:
            bytes1=f.read(1)
            array=[]
            while len(bytes1)>0:
                libs[count]+=[bytes1]
                #print(libs[count])
                bytes1=f.read(1)
            print("done collecting "+str(count))
            avg+=len(libs[count])
            #print(len(libs))
        count+=1
    avg/=len(droppedFiles)-1
    avg=int(avg)
    count=0
    libra=[]
    x1=9000
    x2=10000
    while count<avg/100:
        rand=random.randrange(x2,x2+15000)
        pick=random.randrange(0,len(droppedFiles))
        libra+=libs[pick][x1:x2]
        x1=x2
        x2=x2+10000
        count+=1
    with open("Output.mp3","wb") as f:
        for a in libra:
            f.write(a)
            
    print("done")
else:
    print("You need to drop multiple mp3 files on this script")
input()