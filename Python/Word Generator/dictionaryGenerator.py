a=""
with open("words.txt","r") as f:
	a=f.read().replace("\n","").lower().replace("  "," ")

b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']	

def getWordStats(a,l):
	#d["a"]={"count":,"a":,"b":,"c":,"d":,"e":,"f":,"h":,"i":,"j":,"k":,"l":,"m":,"n":,"o":,"p":,"q":,"r":,"s":,"t":,"u":,"v":,"w":,"x":,"y":,"z":," ":}
	for y in b:
		print('d["'+y+l+'"]={',end="")
		print('"count":',a.count(y+l),',',end="")
		for x in b:
			print('"'+x+'":',a.count(y+l+x),',',end="")
		print("}")
for x in b:
        getWordStats(a,x)
