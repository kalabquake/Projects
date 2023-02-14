import sys

def main():
    file = sys.argv[1]
    bits=[]
    outputSize=int(input('Enter output size(in mb): '))
    with open(file,"rb") as f:
        bits+=f.read()
        f.close()
    #print(len(bits))
    count=0
    chunksize=int(1048526*outputSize)
    a=0
    shift=chunksize
    while a<len(bits):
        with open("output"+str(count),"wb") as f:
            for b in bits[a:shift]:
                #print(bytes([b]))
                f.write(bytes([b]))
            f.close()
        #if(a==0):
        #    a+=1
        a+=chunksize
        shift+=chunksize
        count+=1
        if(shift>len(bits)):
            shift=len(bits)
    #print(count)
    #input()
    
if(len(sys.argv)<2):
    print("You need to drag and drop a file onto this")
    input("Press enter to exit")
else:
    main()