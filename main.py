import openai
import os
openai.api_key = "YOUR_API_KEY"

def load_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

file_path = 'prompt.txt'
prompt = load_text_file(file_path)

response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You extract information from documents and return json objects"},{"role": "user", "content": prompt}])
print(response["choices"][0]["message"]["content"])