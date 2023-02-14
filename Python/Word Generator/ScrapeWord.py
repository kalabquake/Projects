import requests

for x in range(5,542):
    r=requests.get("https://www.bestwordlist.com/allwordspage"+str(x)+".htm")

    html= r.content.split(b'</')
    words=[]

    for x in html:
        if(b'span class=mot' in x):
            words+=[str(x).replace("b'h2><p><span class=mot>","").replace("b'h2><p><span class=mot2>","").replace("b'span><span class=mot>","").replace("b'span><span class=mot2>","")]

    #print(r)
    with open("words.txt","a") as f:
        for x in words:
            f.write(x.replace("'","").replace("bp><p><span class=mot>","").replace("  "," "))
        f.write("\n")