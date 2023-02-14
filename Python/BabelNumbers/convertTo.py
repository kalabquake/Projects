import math
import sys

def pow(n,d):
        val=n
        if(d==0):
                return 1#funny math
        for x in range(0,d-1):
                val*=n
        return val

conversion=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ',',','.','!','?','&','*','(',')','-','_','+','=','[',']','#','/','\'','"')
a=input("Enter text:\n")
a=a.lower()
pos=0
val=0
for x in a:
	if not x in conversion:
		input(x+' not in conversion list... Quiting\n<press enter to exit>')
		break
		#sys.exit(0)
	#print("55^"+str(pos)+"*"+str(conversion.index(x))+" = "+str(pow(len(conversion),pos)*conversion.index(x)))
	val+=int(pow(len(conversion),pos)*conversion.index(x))#base*pos+val
	#print("val:",val)
	pos+=1
	
print(val)
