from langchain import PromptTemplate, LLMChain
import chainlit as cl
from langchain import HuggingFaceHub
import PySimpleGUI as sg
from deep_translator import GoogleTranslator

def select_language(window, event, values):
    global language
    language = [values[event]]  # Convert the selected language to a list
    # Do something with the selected language

sg.theme('DefaultNoMoreLines')

layout = [[sg.Text('Select Language'), sg.Combo(['English', 'Spanish', 'French'], key='-LANGUAGE-')],
          [sg.Button('OK', key='-OK-')]]

window = sg.Window('Language Selector', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == '-OK-':
        break
    elif event == '-LANGUAGE-':
        select_language(window, event, values)

window.close()
# # Change the language argument to a string
language = "Spanish"

# Convert the list to a tuple
language = tuple(language)
repo_id = "tiiuae/falcon-7b-instruct"
# Create the HuggingFaceHub object
llm = HuggingFaceHub(
huggingfacehub_api_token='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',
repo_id=repo_id,
model_kwargs={"temperature":0.3, "max_new_tokens":1024}
)


template = """ Task: write a specific answer to question related to education only, giving reference to the textbooks.
Topic: education
Style: Academic
Tone: Curious
Audience: 5-10 year olds
Length: 1 paragraph
Format: Text
Here's the question. {question}
"""


@cl.on_chat_start
def main():
    # Instantiate the chain for that user session
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    # Store the chain in the user session
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message: cl.Message):
    # Retrieve the chain from the user session
    llm_chain = cl.user_session.get("llm_chain")  # type: LLMChain

    # Call the chain asynchronously
    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])
    # english = res["text"]
    translator = GoogleTranslator(source='auto', target='es')
    print(translator.translate(res["text"]))
    await cl.Message(content=translator.translate(res["text"])).send()
