import gradio as gr
from PIL import Image

def modifications(image): #takes file as input
    return image.rotate(45) #modifies image / output


def greet(question): #replace this with the function that can answer the question
    return "Did you ask " + question + "?" #returns the answer to the question

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Digitialise It!
    """)

    with gr.Row("Upload your File"):
        input=gr.Image()
        output=gr.Image()
        upload_btn=gr.Button("Upload")
        upload_btn.click(fn=modifications,inputs=input, outputs=output)
    with gr.Row("Ask a Question"):
        question = gr.Textbox(label="Question") #textbox for question
        answer = gr.Textbox(label="Answer") #textbox for answer
        enter_btn = gr.Button("Enter") #enter button 
        enter_btn.click(fn=greet,inputs=question,outputs=answer) #displays answer to question when enter is clicked

    

demo.launch() 