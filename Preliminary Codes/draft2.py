# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:02:21 2024

@author: Maanas
"""

from openai import OpenAI
import base64
import requests
from IPython.display import display
from IPython.display import Image as ip_image
from PIL import Image

# OpenAI API Key
# api_key = "$"

#%% Function to encode the image from path

# Function to display image image from file
def display_image_file(image_path):
    myImage = Image.open(image_path)
    return myImage.show()

# Function to encode the image from file
def encode_image_file(image_path):
  with open(image_path, "rb") as image_file:
      display_image_file(image_path)
      return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "C:\\Users\Maanas\OneDrive - Imperial College London\Blackboard\Research Computing\Project\\test notes.jpg"

# Getting the base64 string
base64_image = encode_image_file(image_path)

#%% Image from URL

# Function to display image image from url
def display_image_url(url):
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Display the image
        display(ip_image(response.content))
    else:
        print("Failed to retrieve the image.")

# Function to encode the image from url
def encode_image_url(url):
    display_image_url(url)
    return base64.b64encode(requests.get(url).content)

# URL of image
image_url = "https://www.sccsikar.com/blog/wp-content/uploads/2022/08/7-4-745x1024.jpg"

# Getting the base64 string
base64_image = encode_image_url(image_url)

#%% GPT 4V text to image - normal instructions

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s written in these notes? Please translate handwriting into text precisely, and write them into Latex so I can directly copy and paste into Latex."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 1000
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())

#%% Save extracted text to file

extracted_text = response.json()

f = open("extracted_text.txt","a")

f.write("\n")
f.write("\n")
f.write("---"*30)
f.write("\n")
f.write("\n")

f.write(extracted_text)
f.close()

#%% GPT 4V text to image - extra instructions - look for boxes, etc

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s written in these notes? Please translate handwriting into text precisely, and write them into Latex so I can directly copy and paste into Latex. Locate all the handwritten text which has been boxed, highlighted, written in bold, underlined, italicised, or marked distinctly (for example, using stars) and in the Latex file, write them in a seperate section."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 1000
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())

#%% Save extracted text to file

extracted_text = response.json()

f = open("extracted_text.txt","a")

f.write("\n")
f.write("\n")
f.write("---"*30)
f.write("\n")
f.write("\n")

f.write(extracted_text)
f.close()


#%% Claude text to image

#%% Save extracted text to file

extracted_text = response.json()

f = open("extracted_text.txt","a")

f.write("\n")
f.write("\n")
f.write("---"*30)
f.write("\n")
f.write("\n")

f.write(extracted_text)
f.close()


#%% Gemini text to image

from vertexai.preview.generative_models import GenerativeModel, Part

gemini_pro_vision_model = GenerativeModel("gemini-1.0-pro-vision")
image = Part.from_uri("image_url", mime_type="image/jpeg")
model_response = gemini_pro_vision_model.generate_content(["What’s written in these notes? Please translate handwriting into text precisely, and write them into Latex so I can directly copy and paste into Latex. Locate all the handwritten text which has been boxed, highlighted, written in bold, underlined, italicised, or marked distinctly (for example, using stars) and in the Latex file, write them in a seperate section.", image])

print("model_response\n",model_response)


#%% Save extracted text to file

extracted_text = response.json()

f = open("extracted_text.txt","a")

f.write("\n")
f.write("\n")
f.write("---"*30)
f.write("\n")
f.write("\n")

f.write(extracted_text)
f.close()

#%% GPT 4 interaction - questions

def ask_questions_from_file(file_path, questions):
    # Read file content
    with open(file_path, 'r') as file:
        file_content = file.read()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Using the uploaded document as your primary data source to answer a few questions."
                    },
                    {
                        "type": "text",
                        "text": file_content
                    }
                ]
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())

#%%%

# Example usage
file_path = '...'

questions = [
    "What is the main idea of this document?",
    "Can you summarize the key points?",
    "What are the implications of this information?"
]

ask_questions_from_file(file_path, questions)

#%% Claude interaction - questions

def ask_questions_from_file(file_path, questions):
    # Read file content
    with open(file_path, 'r') as file:
        file_content = file.read()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Using the uploaded document as your primary data source to answer a few questions."
                    },
                    {
                        "type": "text",
                        "text": file_content
                    }
                ]
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())

#%%%

# Example usage
file_path = '...'

questions = [
    "What is the main idea of this document?",
    "Can you summarize the key points?",
    "What are the implications of this information?"
]

ask_questions_from_file(file_path, questions)

#%% Gemini interaction - questions

def ask_questions_from_file(file_path, questions):
    # Read file content
    with open(file_path, 'r') as file:
        file_content = file.read()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Using the uploaded document as your primary data source to answer a few questions."
                    },
                    {
                        "type": "text",
                        "text": file_content
                    }
                ]
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())

#%%%

# Example usage
file_path = '...'

questions = [
    "What is the main idea of this document?",
    "Can you summarize the key points?",
    "What are the implications of this information?"
]

ask_questions_from_file(file_path, questions)

