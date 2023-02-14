import openai

# Supply your API key
openai.api_key = "sk-..."

# Call the create method with a prompt and other parameters
image_resp = openai.Image.create(prompt="a cat sitting on a couch, watercolor", size="512x512")

# Print the image URLs
print(image_resp['data'])
