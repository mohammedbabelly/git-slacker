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
        messages = re.findall(r'\d+\.\s*(.+)', commit_text)
        return messages
    except Exception as e:
        return f"Error while sending request to ollama! {str(e)}"


def prepare_prompt(diff):
    return f"""
You are a helpful AI assistant tasked with generating concise and clear commit messages. You will be given the output of a `git diff --staged` command, which describes the changes made to the codebase. Your task is to generate exactly 4 suggested commit messages that accurately capture the essence of these changes and the file names. The messages should be concise and to the point, reflecting best practices for commit messages.

Please format the output as follows:

1. [First commit message]
2. [Second commit message]
3. [Third commit message]
4. [Fourth commit message]

Here is the diff output:

```
{diff}
```

"""
