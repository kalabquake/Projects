import sys
import random

class Question:
    def __init__(self,question,answer,*options):
        self.question=question
        self.answer=answer
        self.options=options
        self.display=[]
    def randomize(self):
        self.display=[]
        self.display.append(self.answer)
        temp=list(self.options[0])
        a=0
        while a<3 and len(temp):
            b=random.randint(0,len(temp)-1)
            self.display.append(temp[b])
            del temp[b]
            a+=1
        random.shuffle(self.display)

    def show(self):
        self.randomize()
        print(self.question)
        a=97
        for x in self.display:
            print(chr(a)+".  "+x)
            a+=1

    def check(self,guess):
        a=ord(guess.lower())-97
        if(a<0 or a>len(self.display)-1):
            return False
        if(a==0):
            return self.display[0]==self.answer
        if(a==1):
            return self.display[1]==self.answer
        if(a==2):
            return self.display[2]==self.answer
        if(a==3):
            return self.display[3]==self.answer
        
    def getCorrect(self):
        a=0
        while a<len(self.display):
            if(self.display[a]==self.answer):
                return chr(a+97)
            a+=1



def interpretData(data):
    data=data.split('" ')
    a=0
    question=''
    answer=''
    options=[]
    while a<len(data):
        data[a]=data[a].replace('"','')
        if(a==0):
            question=data[a]
        elif(a==1):
            answer=data[a]
        else:
            options.append(data[a])
        a+=1
    #print(question)
    #print(answer)
    #print(options)
    return Question(question,answer,options)
        
        
data=[]

if(len(sys.argv)>1):
	with open(sys.argv[1],'r') as f:
		data=f.read().split('\n')
else:
	name=input("Enter file name: ")
	with open(name,'r') as f:
		data=f.read().split('\n')

q=[]
for x in data:
    q.append(interpretData(x))
random.shuffle(q)
num=1
c=0
for x in q:
    print("#"+str(num)+":")
    x.show()
    guess='A'
    #while 'a' not in guess and 'b' not in guess and 'c' not in guess and 'd' not in guess:
    while(ord(guess)-97<0 or ord(guess)-97>=len(x.display)):
        guess=input('Enter guess: ')
        if(len(guess)>0):
            guess=guess.replace('\n','').replace(' ','')[0].lower()
        #if('a' not in guess and 'b' not in guess and 'c' not in guess and 'd' not in guess):
        #    print('Invalid selection. Please try again')
        #    continue
        if(ord(guess)-97>=0 and ord(guess)-97<len(x.display)):
            break
        else:
            print('Invalid Selection')
            continue
    a=x.check(guess)
    if(a):
        print("Correct\n")
        c+=1
    else:
        print("Incorrect.\nAnswer was: "+x.getCorrect()+"\n")
    num+=1
percent=str((c/len(q))*100)[:5]
print(str(c)+"/"+str(len(q))+" correct. \n"+percent+"%")
    
#q=interpretData(data[0])
#q.show()
#q=Question("question","answer",['b','c'])
#q.randomize()
#.show()
input('<press enter to exit>')
