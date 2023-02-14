import requests

"""
# Set the API endpoint and the API key
endpoint = "https://api.openai.com/v1/text-davinci/completions"
api_key = "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"

# Set the input text and other request parameters
prompt = "The quick brown fox jumps over the lazy dog."
model = "text-davinci-002"
max_tokens = 256

# Make the request
response = requests.post(
    endpoint,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    },
    json={
        "prompt": prompt,
        "model": model,
        "max_tokens": max_tokens,
    },
)

# Print the response
print(response.json())
"""

import openai
openai.api_key = "key"

# list engines
engines = openai.Engine.list()

# print the first engine's id
for x in engines.data:
    print(x.id)

print("\n\nresults:")

model_engine = "text-davinci-003"

# Set the prompt
prompt = "How do I calculate prime numbers in python?"

# Generate completions
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)

# Get the first completion
completion = completions.choices[0].text

# Print the completion
print(completion)
