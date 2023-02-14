import sys

symbols=['.',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',',','"','?','(',')','1','2','3','4','5','6','7','8','9','0','[',']',"'",'!','$','#','@','^','&','*','-','+','=','\\','|',';',':','/']
a=[]
sys.argv.append('Reading3.txt')
with open(sys.argv[1],'r') as f:
   a=f.read().split('\n')


b=''
for x in a:
    #for i in x:
        #for j in i:
            #print(str(j)+" in symbols: " + str(j in symbols))
            #if(j.lower() in symbols):
    b+=x.replace('â€™',"'").replace('”','"').replace("“",'"')
            #else:
            #    b+="'"
    b+=' '
with open('output.txt','w') as f:
    f.write(b)

input('press enter')
