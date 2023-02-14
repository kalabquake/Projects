import sys

def main():
    #print(sys.argv[1:])
    files=sys.argv[1:]
    #print(len(files))
    nam=input("Enter name for file: ")
    with open(nam,"wb") as f:
        for file in files:
            with open(file,"rb") as g:
                f.write(g.read())
                g.close()
        f.close()
    input()
    
    
if(len(sys.argv)<2):
    print("You need to drop multiple files onto this script!")
    input("press enter to exit")
elif(len(sys.argv)==2):
    print("This is a file reconstructor! You probably want to drop more than 1 file onto this script")
    input("press enter to exit")
else:
    main()