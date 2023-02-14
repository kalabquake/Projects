import random


d=""
with open("words.txt",'r') as f:
    d=f.read().replace("\n","").lower().replace("  "," ")

b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
prevLetter = " "#starts as space and resets to just space if a space gets added
curLetter = random.choice(b)
string=""

a=0
while(a<2000):
    string+=curLetter
    i=random.randrange(d.count(prevLetter+curLetter))
    sum=0
    for x in b:
        sum+=d.count(prevLetter+curLetter+x)
        if(sum>i):
            prevLetter+=curLetter
            if(x==" "):
                prevLetter=""
            curLetter=x
            break
    a+=1

print(string)