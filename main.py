import asyncio
import datetime
import json
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from rich.console import Console
import openai


load_dotenv()

LOG_DIR = Path("log")
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    filename=LOG_DIR / "conversation.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

# Terminal colors can break in some environments
os.environ.setdefault("TERM", "xterm")


class ChatAssistant:
    def __init__(self, log_file: Path = Path("conversation_log.json")) -> None:
        self.console = Console(color_system=None)
        self.log_file = log_file
        self.conversation_log = self._load_log()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def _load_log(self):
        if self.log_file.exists():
            try:
                with self.log_file.open("r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def _save_log(self):
        with self.log_file.open("w") as f:
            json.dump(self.conversation_log, f, indent=4)

    async def _query_openai(self, messages):
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response["choices"][0]["message"]["content"]

    async def chat(self) -> None:
        os.system("clear")
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        logging.info(json.dumps(messages[0]))

        while True:
            user_input = input("User: ")
            user_message = {"role": "user", "content": user_input}
            messages.append(user_message)
            logging.info(json.dumps(user_message))

            if user_input.lower() == "exit":
                break

            self.console.print("Assistant:", end=" ")
            assistant_text = await self._query_openai(messages)
            assistant_message = {"role": "assistant", "content": assistant_text}
            messages.append(assistant_message)
            highlighted = highlight(assistant_text, PythonLexer(), TerminalFormatter())
            self.console.print(f" {highlighted}")

        self.conversation_log.append(
            {
                "conversation": messages,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        self._save_log()
        self.console.print("Good bye")


if __name__ == "__main__":
    assistant = ChatAssistant()
    asyncio.run(assistant.chat())
