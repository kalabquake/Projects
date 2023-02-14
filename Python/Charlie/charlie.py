import random
from io import BytesIO
import discord
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

client = discord.Client()


@client.event
async def on_message(message):
    # Check if the message starts with '!meme'
    if message.content.startswith('!meme'):
        # Split the message into a list of words
        s = message.content.replace("!meme ","")
        words = s.split("|")
        if(len(words)<2):
            await message.channel.send("invalid format: ``!meme top text | bottom text``")
            return
        # Get the text for the top and bottom of the meme
        top_text = words[0]
        bottom_text = words[1]

        # Check if the message has an image attached
        if message.attachments:
            # Get the first image in the list of attachments
            image_url = message.attachments[0].url
        else:
            # If no image was attached, get a random image based on the first word of the prompt
            image_url = f"https://source.unsplash.com/featured/?{words[0]}"
            image_url = requests.get(image_url).url
            if (image_url == 'https://images.unsplash.com/source-404?fit=crop&fm=jpg&h=800&q=60&w=1200'):
                print("image not found from prompt text")
            while image_url == 'https://images.unsplash.com/source-404?fit=crop&fm=jpg&h=800&q=60&w=1200':
                random_word = get_random_word()
                # Search for an image using the random word
                print(random_word)
                search_url = f"https://source.unsplash.com/featured/?{random_word}"
                image_url = requests.get(search_url).url
                if (image_url == 'https://images.unsplash.com/source-404?fit=crop&fm=jpg&h=800&q=60&w=1200'):
                    print("removing word:", random_word)
                    removeWord(random_word)

        # Download the image
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))

        # Calculate the size of the font based on the size of the image
        image_width, image_height = image.size
        font_size = int(image_height / 10)

        # Create a drawing context for the image
        draw = ImageDraw.Draw(image)

        nLetters=max(len(top_text),len(bottom_text))
        # Use a truetype font
        fsize=min(int((image.size[0] / nLetters) * 2),int(image.size[0]/15))
        font = ImageFont.truetype("arial.ttf", fsize)

        # Get the width and height of the top and bottom text
        top_text_width, top_text_height = draw.textsize(top_text, font=font)
        bottom_text_width, bottom_text_height = draw.textsize(bottom_text, font=font)

        # Calculate the x-coordinate for the top and bottom text
        top_text_x = (image_width - top_text_width) / 2
        bottom_text_x = (image_width - bottom_text_width) / 2

        # Add the top and bottom text to the image

        #draw.rectangle((top_text_x, top_text_height/5+fsize, top_text_width/1.075+top_text_x, top_text_height/0.85-int(fsize)), fill="black", outline="black")
        draw.text((top_text_x, 0), top_text, font=font, fill=(255, 255, 255))
        draw.text((bottom_text_x, image_height - bottom_text_height*1.4), bottom_text, font=font, fill=(255, 255, 255))

        # Save the image to a buffer
        image_buffer = BytesIO()
        image.save(image_buffer, 'PNG')
        image_buffer.seek(0)

        # Send the image to the channel
        await message.channel.send(file=discord.File(image_buffer, 'meme.png'))

    if message.content.startswith('!randommeme'):
        # Get a random word to use as a search query
        image_url='https://images.unsplash.com/source-404?fit=crop&fm=jpg&h=800&q=60&w=1200'
        while image_url=='https://images.unsplash.com/source-404?fit=crop&fm=jpg&h=800&q=60&w=1200':
            random_word = get_random_word()

            # Search for an image using the random word
            print(random_word)
            search_url = f"https://source.unsplash.com/featured/?{random_word}"
            image_url = requests.get(search_url).url
            if(image_url=='https://images.unsplash.com/source-404?fit=crop&fm=jpg&h=800&q=60&w=1200'):
                print("removing word:",random_word)
                removeWord(random_word)
        print(image_url)

        # Download the image
        image = Image.open(requests.get(image_url, stream=True).raw)

        # Generate a random phrase to use as the top text
        top_text = get_random_phrase()

        # Generate a random phrase to use as the bottom text
        bottom_text = get_random_phrase()

        # Add the text to the image
        draw = ImageDraw.Draw(image)
        nLetters=max(len(top_text),len(bottom_text))
        fsize = min(int((image.size[0] / nLetters) * 2), int(image.size[0] / 15))
        font = ImageFont.truetype("arial.ttf", fsize)
        print(image.size)
        top_text_width, top_text_height = draw.textsize(top_text, font=font)
        bottom_text_width, bottom_text_height = draw.textsize(bottom_text, font=font)

        # Calculate the x-coordinate for centering the text
        top_text_x = (image.width - top_text_width) // 2
        bottom_text_x = (image.width - bottom_text_width) // 2

        # Draw the top text
        draw.text((top_text_x, 0), top_text, font=font, fill=(255, 255, 255))

        # Draw the bottom text
        draw.text((bottom_text_x, image.height - bottom_text_height), bottom_text, font=font, fill=(255, 255, 255))

        # Save the image to a temporary file
        with open("temp.jpg", "wb") as f:
            image.save(f)

        # Send the meme back to the user
        await message.channel.send(file=discord.File("temp.jpg"))

def removeWord(word):
    with open("dictionary.txt","r") as f:
        lines=f.readlines()
    s=''
    for x in lines:
        if(x!=word):
            s+=x
    with open("dictionary.txt",'w') as f:
        f.write(s)

def get_random_word():
    # Open the dictionary file
    with open("dictionary.txt", "r") as f:
        # Read all the lines in the file
        lines = f.readlines()

        # Choose a random line from the file
        return random.choice(lines).strip()


def get_random_words_for_phrase():
    # Get a list of all the words in the dictionary
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    response = requests.get(url)
    words = response.text.split()

    # Choose a random word from the list
    return random.choice(words)

def get_random_phrase():
    # TODO: Return a random phrase from a list of phrases
    numWords=random.randint(2,4)
    s=''
    for x in range(numWords):
        s+=get_random_words_for_phrase()+" "
    return s
client.run('key')