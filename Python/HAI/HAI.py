import discord
import os
import asyncio
import random
import requests
import openai
import time
from better_profanity import profanity

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):

    if message.author == client.user:
        return
        
    print(" Message: "+message.content)
    if message.content.startswith('_'):
        await message.channel.trigger_typing()
        openai.api_key = "key"
        
        profanity.load_censor_words_from_file(r"bannedWords.txt")
        c=message.content[1:]
        if(profanity.contains_profanity(c)):
        
            c=profanity.censor(c)
            
        with open("questions.txt",'a+') as f:
            f.write(c+"\n")
        engines = openai.Engine.list()


        model_engine = "text-davinci-003"

        # Set the prompt
        prompt = c

        # Generate completions
        completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,
                                               temperature=0.5)

        # Get the first completion
        completion = completions.choices[0].text

        # Print the completion
        print("Response: "+completion.strip())
        if(len(completion.strip())<=2000):
            await message.reply("GPT-3: "+(completion.strip()))
        else:
            a=0
            c=''
            while(a<len(completion)):
                c=completion[a:a+1000]
                if(a==0):
                    await message.reply("GPT-3: " + (c.strip()))
                else:
                    await message.reply((c.strip()))
                a+=1000





client.run('client key')
