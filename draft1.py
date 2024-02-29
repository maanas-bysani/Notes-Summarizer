# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 12:11:28 2024

@author: Maanas
"""

#%% imports

from openai import OpenAI
from IPython.display import display
from IPython.display import Image as ip_image
import requests
import base64
import re
import os
import numpy as np

# import pytesseract
from PIL import Image

#%% function to get image from url/link

def display_image_from_url(url):
    # Fetch the image from the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Display the image
        display(ip_image(response.content))
    else:
        print("Failed to retrieve the image.")

#%%  example usage

url = '...'

display_image_from_url(url)

#%% fucntion to get image from system
path = '...'

def display_image_from_file(path):
    myImage = Image.open(path)
    return myImage.show()

display_image_from_file(path)

#%% include openai gpt4V code here

client = OpenAI(max_retries=3,
                   timeout=20.0,)

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[

        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Transcribe this article into markdown."},
                {
                    "type": "image_url",
                    "image_url": url, #replace with path if local file
                },

            ],
        }
    ],
    max_tokens=1500,
)
extracted_text = response.choices[0].message.content
print(extracted_text)

#%% save string to txt

f = open("extracted_text.txt","a")

f.write("\n")
f.write("\n")
f.write("---"*30)
f.write("\n")
f.write("\n")

f.write(extracted_text)
f.close()

#%% q&a interaction

question = '...'



