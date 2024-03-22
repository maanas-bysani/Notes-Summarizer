# Notes-Summarizer Tool

**Research question**
Can machine learning algorithms such as GPT-4V be used to analyse large datasets of student notes to generate master notes for students to use and share to support their learning? 

<br />

**Method**
1) Use GPT4 Vision to extract and process text. Tune parameters to enhance reliability and accuracy.
2) Use LLM Models (GPT, Gemini, Claude) as a Q&A Bot with the extracted text as the primary database.
3) Build a Front End User Interface.

<br />

**Purpose**
Students prefer writing their notes by hand but due to the speed and style of lecturers, notes are often messy and span several pages. In knowing this, our project is to create a tool that allows students to make a digital form of their notes that makes revision and knowledge recall faster.
As part of I-Explore Interdisciplinary Computing Year 2 Module.

<br />

**The final product will be:**
- a webpage with capabilities to upload your notes, extract a summarised version for your reference, and ask questions which the AI answers using information from your notes.
- The AI model will be able to extract important information - this is text that has been explicitly identified in your notes using markers such as text that is underlined, highlighted, italicized, boxed, starred, etc.

**How is this different from ChatGPT/exisiting models:**
- It offers a user-friendly single-webpage interface which streamlines your learning.
- It uses and learns from your notes only. There will be an option to allow the AI model to use the internet to answer questions, but this is not the default setting.
- You can alter between AI models, ex: GPT, Claude, Gemini/Vertex.
- In the future, we hope to use a database of notes from an entire cohort to develop a sort of master summarised notes. This will be compared with official lecture notes from the lecturer for accuracy by the AI model and will be adapted accordingly.
  
<br />

**Folders**
- Characters Testing: Testing a random assortment of Greek alphabets, English alphabets, numbers and simple math operators to determine accuracy of each vision model.
- Final Code: Final versions of the code used. _This still needs further development before full deployment_
- Poster Images: Images and plots used in the poster
- Preliminary Codes: Preliminary versions of the code used.
- Preliminary Images: Images and respective outputs used in the initial phases of the project.
- References: Citations used in the poster.

<br />
<br />
------------------------
<br />
<br />

- Preliminary Codes/irc_ui.py was developed by Kadija (Shows uploaded by Maanas as I moved it around while organising the GitHub).
- All other codes by Maanas with assistance from Norman (mentor).
