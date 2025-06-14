# AI Chat Assistant
This project contains a terminal based chat assistant powered by **OpenAI's GPT-3 API**.  It accepts user input, forwards it to the API and displays the response.  Conversations are persisted so you can review them later.

## Requirements
- Python 3.6+
- OpenAI API key
## Setup
Clone this repository to your local machine and install the dependencies with:
```bash
pip install -r requirements.txt
```
Set your OpenAI API key in a `config.py` file or export it as the environment variable `OPENAI_API_KEY`.
## Dependencies
This project requires the following dependencies which are listed in `requirements.txt`:

- `openai`
- `pygments`
- `rich`
- `python-dotenv`
## Usage
Start a conversation by running `python main.py` from the project root.  The assistant uses an asynchronous workflow so responses are non-blocking while waiting for the API.
```
python main.py
```

The assistant will prompt you for input, and you can type in any message. Once you hit enter, the assistant will send your message to the __OpenAI API__ and return a response. The conversation is logged and stored in `conversation_log.json`.

To exit the conversation, type __"exit"__ and hit enter.

# Enhancements
This chat assistant can be enhanced by adding more functionality, such as handling user input errors, adding more logging details, and improving the formatting of the console output.
