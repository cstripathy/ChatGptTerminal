# AI Chat Assistant
This is a simple AI chat assistant that interacts with users using **OpenAI's GPT-3 API**. The assistant takes user input, sends it to the API and returns a response. The conversation is logged and can be viewed later.

## Requirements
- Python 3.6+
- OpenAI API key
## Setup
Clone this repository to your local machine.
Install the required packages by running `pip install -r requirements.txt`.
Set your OpenAI API key in a `config.py` file or in your environment variables as `OPENAI_API_KEY`.
## Dependencies
This project requires the following dependencies:

- openai
- pygments
- rich
## Usage
To start a conversation with the chat assistant, run `python chat.py` in your terminal.
```
python chat.py
```

The assistant will prompt you for input, and you can type in any message. Once you hit enter, the assistant will send your message to the __OpenAI API__ and return a response. The conversation is logged and stored in `conversation_log.json`.

To exit the conversation, type __"exit"__ and hit enter.

# Enhancements
This chat assistant can be enhanced by adding more functionality, such as handling user input errors, adding more logging details, and improving the formatting of the console output.
