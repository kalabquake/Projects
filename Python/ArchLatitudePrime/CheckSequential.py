lines=[]
with open("primeNumbers.txt","r") as f:
    lines=f.read().split("\n")

previous=0
for x in lines:
    if(x==""):
        continue
    if int(x)>previous:
        previous=int(x)
    else:
        print("Error:"+x)
        break
