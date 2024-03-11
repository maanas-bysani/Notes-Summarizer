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

#%% LLM image to text code

#%%% openai gpt4V code here

# https://github.com/openai/openai-python
# https://platform.openai.com/docs/api-reference?lang=python
# https://medium.com/@felix.lu07/understanding-and-use-cases-of-a-python-script-for-image-data-extraction-with-openais-gpt-4-vision-f0b5393200e3
    

client = OpenAI(api_key=($))

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {"role": "user",
            "content": [{"type": "text", 
                         "text": "Extract all text in this image and return in markdown format."},
                {"type": "image_url",
                 "image_url": url, #replace with path if local file
                },
            ],
        }
    ],
    max_tokens=500,
    timeout=20.0
)

extracted_text = response["choices"][0]["message"]["content"][0]["text"]

# extracted_text = response.choices[0].message.content.text

# extracted_text = response.choices[0].message.content
print(extracted_text)


#%%% gemini code here

# https://medium.com/google-cloud/text-extraction-from-image-using-google-gemini-6b9d9989fa84

from vertexai.preview.generative_models import GenerativeModel, Image
import json
import pandas as pd

model = GenerativeModel("gemini-pro-vision")
image = Image.load_from_file(path)
response = model.generate_content(
    [image, "Extract all text in this image and return in markdown format."]
    )

extracted_text = response.text

print(extracted_text)


#%%% gemini code here v2

# https://cloud.google.com/vertex-ai/docs/samples/aiplatform-gemini-safety-settings#aiplatform_gemini_safety_settings-python

import PIL.Image
img = PIL.Image.open(https://www.sccsikar.com/blog/wp-content/uploads/2022/08/7-4-745x1024.jpg)
img

url = 'https://www.sccsikar.com/blog/wp-content/uploads/2022/08/7-4-745x1024.jpg'

display_image_from_url(url)

from vertexai import generative_models

def generate_text(project_id: "notes-summarizer-416813", image: str) -> str: #location: str,
    # Initialize
    vertexai.init(project=project_id)

    # Load model
    model = generative_models.GenerativeModel("gemini-1.0-pro-vision")

    # Generation config
    config = {"max_output_tokens": 2048, "temperature": 0.4, "top_p": 1, "top_k": 32}

    # Safety config
    safety_config = {
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }

    # Generate content
    responses = model.generate_content(
        [image, "Extract all text in this image and return in markdown format."],
        generation_config=config,
        stream=True,
        safety_settings=safety_config,
    )

    text_responses = []
    for response in responses:
        print(response.text)
        text_responses.append(response.text)
    return "".join(text_responses)

    extracted_text = text_responses

    print(extracted_text)


#%%% claude code here


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



