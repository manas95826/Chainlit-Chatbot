# Chainlit Chatbot

## Introduction

Chainlit Chatbot is a Python script that leverages the Chainlit library for building a chatbot. The chatbot includes a language selection feature and utilizes the Hugging Face model for generating responses. Additionally, it integrates language translation using the Translate library.

## Installation

To use the chatbot, follow these steps:

1. Install the required Python libraries:

```bash
pip install langchain chainlit PySimpleGUI translate
Clone the repository:
bash
Copy code
git clone https://github.com/themanas95826/Chainlit-Chatbot.git
cd Chainlit-Chatbot
Run the chatbot script:
bash
Copy code
python chatbot_script.py
Usage
Upon running the script, a language selection window will appear. Choose a language from the dropdown menu, and the chatbot will generate responses accordingly.

Hugging Face Model
The chatbot uses the Hugging Face model with the following parameters:

Repository ID: tiiuae/falcon-7b-instruct
Model Parameters: temperature=0.3, max_new_tokens=1024
Translation Feature
The chatbot includes a language translation feature powered by the Translate library. Responses are translated based on the selected language.

Examples
Here are examples of running the chatbot with different language selections:

English
Spanish
French
Contributing
Contributions to the project are welcome. Feel free to submit issues and pull requests.

License
This project is licensed under the MIT License.
