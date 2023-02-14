import discord
import os
from youtubesearchpython import VideosSearch
import pytube as pt
import os
import asyncio
import random


client = discord.Client()

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def endSong(guild, path,vc):
    queue=None
    if(guild!=None):
        queue = getQueueArray(guild)
    if(os.path.exists(path)):
        #if it is in voice and the song isn't in queue, or if it is disconnecting
        if((guild!=None and path not in queue) or guild == None):
            os.remove(path)
    if(guild!=None and queue!=None and len(queue)>0):
        try:
            asyncio.run_coroutine_threadsafe(playNext(guild,vc),client.loop)
        except Exception as e:
            log.info("Play next song failed: %s", e)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello '+message.author)

    if message.content.startswith('$play'):
        await play(message)

    if message.content.startswith('$disconnect'):
        await disconnect(message)

    if message.content.startswith('$skip'):
        await skip(message)

    if message.content.startswith('$clearQueue'):
        await clearQueue(message)

    if message.content.startswith('$getQueue'):
        await getQueue(message)

    if message.content.startswith('$pause'):
        await pause(message)

    if message.content.startswith('$resume'):
        await resume(message)

    if message.content.startswith('$test'):
        await sendAudioPacket(message)

    if message.content.startswith('$help'):
        await message.channel.send("```$help - shows this menu\n```")



        
async def play(message):
    cont=message.content[len("$play "):].strip()

    #Error catching
    if(cont==""):
        await message.channel.send('Error: format ``$play title`` or ``$play URL``')
        return
    if( not message.author.voice):
        await message.channel.send("You aren't in voice...")
        return
    
    #URL fetching, if necessary
    URL=False
    u=''
    if("?v=" in cont):
        URL=True
        u=cont
    if(not URL):
        vs = VideosSearch(cont,limit=1)
        u="https://www.youtube.com/watch?v="+vs.result()['result'][0]['id']

    #voice connecting
    channel = message.author.voice.channel
        #possible to reduce length here, but I will avoid doing that for now
        #clientvcchannels
    cvccs=[]
    for x in client.voice_clients:
        cvccs+=[x.channel]
    if(message.author.voice.channel not in cvccs):
        vc = await channel.connect()
        await clearQueue(message,True)#fix the queue incase I messed up and reset the bot without clearing the queue
    else:
        vc=client.voice_clients[cvccs.index(message.author.voice.channel)]
    #get server for queue stuff...
    server = message.guild

    
    #audio collecting
    #await message.channel.send("Attempting to download from ``"+u+"`` as an mp3, please standby")
    yt=pt.YouTube(u)
    t = yt.streams.filter(only_audio=True)
    #USE HERE TO REMOVE SPECIAL CHARACTERS SO IT DOESN'T BREAK
    title=yt.title.replace('"','').replace("*","").replace("|",'').replace(":","").replace("/","").replace("?","")
    for x in title:
        if(ord(x)>255):
            title.replace(x,'')
    if(not os.path.exists(os.getcwd()+"\\"+str(server.id)+" "+title+".mp4") and not os.path.exists(os.getcwd()+"\\"+title+".mp4") ):
        path=t[0].download(filename=str(server.id)+" "+title+".mp4")
    if(not os.path.exists(os.getcwd()+"\\"+str(server.id)+" "+title+".mp4")):
        os.rename(path,os.getcwd()+"\\"+str(server.id)+" "+title+".mp4")
    elif(os.path.exists(os.getcwd()+"\\"+title+".mp4")):
        os.remove(os.getcwd()+"\\"+title+".mp4")
    path=os.getcwd()+"\\"+str(server.id)+" "+title+".mp4"


    if((not vc.is_playing() and not vc.is_paused()) and vc.is_connected() and len(getQueueArray(server))==0):
        vc.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(server, path,vc))
        vc.source = discord.PCMVolumeTransformer(vc.source, 1)
    #push into queue
    else:
        #await message.channel.send("Already playing a song, so uh, tell Belfyr make the queue...")
        await message.channel.send("Adding ``"+yt.title+"`` to queue")
        await pushQueue(server,path)
        return
    await message.channel.send("Playing ``"+yt.title+"``")#file['title']+"``")


#manage song queue
async def pushQueue(server,path):
    with open(str(server.id)+"queue.txt","a") as f:
        f.write(path+"\n")
async def popQueue(server):
    lines=[]
    popped=''
    with open(str(server.id)+"queue.txt","r") as f:
        lines=f.read().split("\n")
    if(lines[0]==""):
        return None
    with open(str(server.id)+"queue.txt","w") as f:
        popped=lines[0]
        lines=lines[1:]
        s=''
        for x in lines:
            if(x!=""):
                s+=x+"\n"
        f.write(s)
    return popped
async def clearQueue(message,automatic=False):
    server=message.guild
    if(not automatic):
        await message.channel.send("Clearing queue")
    lines=[]

    if(os.path.exists(str(server.id)+"queue.txt")):
        with open(str(server.id)+"queue.txt","r") as f:
            lines=f.read().split('\n')

    for x in lines:
        endSong(None,x,None)
    with open(str(server.id)+"queue.txt","w") as f:
        f.write("")

#helper function
async def getVC(message):
    channel = message.author.voice.channel
    server = message.guild
    cvccs=[]

    if(len(client.voice_clients)==0):
        return None
    
    for x in client.voice_clients:
        cvccs+=[x.channel]
    if(message.author.voice.channel in cvccs):
        vc=client.voice_clients[cvccs.index(message.author.voice.channel)]
        return vc
    else:
        return None
#helper function. Similar to getQueue, but used by functions rather than users
def getQueueArray(server):
    lines=[]
    with open(str(server.id)+"queue.txt","r") as f:
        lines=f.read().split('\n')
    l=[]
    for x in lines:
        if(x!=""):
            l+=[x]
    return l


async def getQueue(message):
    lines=[]
    server=message.guild
    with open(str(message.guild.id)+"queue.txt","r") as f:
        lines=f.read().split('\n')
    s=''
    for x in lines:
        if(x==""):
            continue
        s+=x[len(os.getcwd()+"\\"+str(server.id)+" "):].replace(".mp4","")+"\n"
    if(len(s.strip())>0):
        await message.channel.send(s)
    else:
        await message.channel.send("Queue is empty")

      
async def skip(message):
    channel = message.author.voice.channel
    server = message.guild
    notInVC="I'm not in voice..."

    vc= await getVC(message)
    
    if(vc != None):
        if(not vc.is_playing() and not vc.is_paused()):
            await message.channel.send("I'm not currently playing anything...")
            return
        await message.channel.send("Skipping...")
        vc.stop()



        
    else:
        await message.channel.send(notInVC)
        return



async def playNext(guild,vc):

    if(guild==None or vc == None):
    
        return

    queue = getQueueArray(guild)
    if(len(queue)==0):
        #print("queue empty")
        return
    path=await popQueue(guild)
    #print(path)
    vc.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path, vc))
    vc.source = discord.PCMVolumeTransformer(vc.source, 1)



async def disconnect(message):
    channel = message.author.voice.channel
    server = message.guild
    await clearQueue(message,True)#if leave voice, empty queue
    
    notInVC="I can't disconnect from something I'm not connected to..."
    vc= await getVC(message)
    
    if(vc!=None):
        await vc.disconnect()
    else:
        await message.channel.send(notInVC)
        return

async def pause(message):
    channel = message.author.voice.channel
    server = message.guild
    
    notInVC="I'm not in voice..."
    vc = await getVC(message)
    if(vc==None):
        await message.channel.send(notInVC)
        return
    if(vc.is_paused()):
        await message.channel.send("Already paused...")
        return
    if(vc.is_playing()):
        await message.channel.send("Pausing...")
        vc.pause()
        return
    else:
        await message.channel.send("I'm not playing anything...")
        return

async def resume(message):
    channel = message.author.voice.channel
    server = message.guild
    
    notInVC="I'm not in voice..."
    vc = await getVC(message)
    if(vc==None):
        await message.channel.send(notInVC)
        return
    if(vc.is_playing()):
        await message.channel.send("Already playing...")
        return
    if(vc.is_paused()):
        await message.channel.send("Resuming...")
        vc.resume()
        return
    else:
        await message.channel.send("I'm not playing anything...")
        return

async def sendAudioPacket(message):
    channel = message.author.voice.channel
    server = message.guild
    
    s=b''
    with open('sample.mp4','rb') as f:
        s=f.read()
    vc = await getVC(message)
    vc.send_audio_packet(s)

client.run('key')
