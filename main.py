import openai
import datetime
import time
import os
from rich.console import Console
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
import logging
import json
from dotenv import load_dotenv

load_dotenv()

# Set up logging configuration
logging.basicConfig(filename='conversation.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# Set the TERM environment variable to xterm
os.environ["TERM"] = "xterm"

# Initialize OpenAI client
openai.api_key = os.getenv('OPENAI_API_KEY')
print(os.environ.get('OPENAI_API_KEY'))
# Define conversation log
conversation_log = []

console = Console(color_system=None)


# Define chat function
def chat():
    os.system('clear')
    # Define conversation log entry
    conversation_log_entry = {}

    # Define messages list
    messages = []

    # Define system message
    system_message = {"role": "system", "content": "You are a helpful assistant."}
    messages.append(system_message)

    # logging initial system message
    logging.info(json.dumps(system_message))

    # Loop through conversation
    while True:
        # Get user input
        user_input = input("User: ")

        # Add user message to messages list
        user_message = {"role": "user", "content": user_input}
        messages.append(user_message)

        # logging initial user message
        logging.info(json.dumps(user_message))

        # Check for exit command
        if user_input.lower() == "exit":
            break

        console.print("Assistant:", end=" ")
        # Query OpenAI for response
        openai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Get OpenAI response
        openai_response_text = openai_response['choices'][0]['message']['content']

        # Add assistant message to messages list
        assistant_message = {"role": "assistant", "content": openai_response_text}
        messages.append(assistant_message)

        # Clear screen before printing assistant response
        # os.system('cls' if os.name == 'nt' else 'clear')

        highlighted_code = highlight(openai_response_text, PythonLexer(), TerminalFormatter())
        console.print(f" {highlighted_code}")

    # Add conversation to conversation log entry
    conversation_log_entry["conversation"] = messages

    # Add timestamp to conversation log entry
    conversation_log_entry["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add conversation log entry to conversation log
    conversation_log.append(conversation_log_entry)

    # Print final message
    console.print("Good bye")


if __name__ == "__main__":
    chat()
