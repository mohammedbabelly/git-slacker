import requests
import json
import re

llama_url = "http://localhost:11434/api/generate"


def suggest_commit_messages(diff) -> list[str]:
    try:
        print("Crafting a commit message, ya lazy...")
        prompt = prepare_prompt(diff)

        payload = {"model": "llama3.1:latest", "prompt": prompt, "stream": False}
        headers = {"content-type": "application/json"}
        response = requests.post(llama_url, headers=headers, data=json.dumps(payload))
        commit_text = response.json()["response"]

        return re.findall(r'\d+\.\s"([^"]+)"', commit_text)
    except Exception as e:
        return f"Error while sending request to ollama! {str(e)}"


def prepare_prompt(diff):
    return f"Given a Git diff describing {diff}, what are four clear and concise commit messages that captures the essence of these changes? Don't be verbose, only return the four suggested commit messages in this format (1. \n 2. \n 3. \n 4.)"
