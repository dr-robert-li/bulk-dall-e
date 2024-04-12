import logging
from openai import OpenAI
import requests
import os
import time

fileloc = input('Input prompt file location...\n')
user_key = input('Input your OpenAI API Key...\n')
set_temp = input('Input temperature from 0.0 to 2.0 with anything above 0.8 as being a bit nutty...\n')
context = input('Type any additional context you wish to provide the prompts e.g. Create an expanded prompt of no more than 40 words to create a high quality and realistic photo\n')

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

client = OpenAI(api_key=user_key)

logging.basicConfig(level=logging.INFO)

print("Generating images using DALL-E 3...")

directory = "./images/"
if not os.path.exists(directory):
    os.makedirs(directory)

with open(fileloc) as file:
    while line := file.readline():
        start_time = time.time()
        print("=====>" + line.rstrip())

        prompt_context = context + " based on %s" % line
         
        response = client.chat.completions.create(
            model="gpt-4",
            n=1,
            temperature=float(set_temp),
            messages=[
                {"role": "system", "content": "You are an assistant that creatively expands prompts."},
                {"role": "user", "content": prompt_context},
            ]
        )

        # PROMPT = response['choices'][0]['message']['content']

        PROMPT = response.choices[0].message.content
        print("EXPANDED PROMPT: " + PROMPT)

        response = client.images.generate(
            model="dall-e-3",
            prompt=PROMPT,
            size="1792x1024",
            # quality="standard",
            # style="natural",
            n=1,
        )

        image_url = response.data[0].url
        print("IMAGE URL: " + image_url)
        
        print("Downloading...")
        image_file = requests.get(image_url)
        clean_line = line.strip()
        filename = "./images/%s.png" % clean_line
        open(filename, 'wb').write(image_file.content)

        end_time = time.time()
        elapsed = end_time - start_time
        print("TIME TO COMPLETE OPERATION (sec): ", elapsed)
        time.sleep(30)