import openai
import os
import re

api_key = os.getenv("OPENAI_API_KEY") # gonna have to get openai key 
print(f"API Key: {api_key}")  # Debugging line

with open('systemPrompt.txt', 'r') as file:
    systemPrompt = file.read()

with open('outputFormat.txt', 'r') as file:
    outputFormat = file.read()

userPrompt = input("Please provide the following details: Name of the location | Description of the location and its importance | Approximate location (continent, country, state, city)")

completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": userPrompt},
        {"role": "assistant", "content": outputFormat}
        ]
)

assistant_response = completion['choices'][0]['message']['content']

print(assistant_response)

rgb_values = re.findall(r'rgb\((\d+), (\d+), (\d+)\)', assistant_response)

rgb_list = [(int(r), int(g), int(b)) for r, g, b in rgb_values]

print(rgb_list)
