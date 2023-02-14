import math
import time

lines =[]
with open("primeNumbers.txt","r") as f:
    lines=f.read().split()

print(len(lines),"prime numbers in list")
print("Final prime in list:",lines[len(lines)-1])


t=time.time()
i=2#Start at prime number 5
#i=int(input("Enter starting index: "))
while i<len(lines):
    n=int(lines[i])
    lim=math.sqrt(n)
    j=0
    prime=True
    #print("currently inspecting",n)
    while int(lines[j])<=lim:
        if(n%int(lines[j])==0):
            prime=False
            break
        j+=1
    if(not prime):
        print("Non-prime found:",n)
        break
    if(i==len(lines)-1):
        print("Checked the whole list!!")
    i+=1
print("execution time:",time.time()-t)
#21073007
