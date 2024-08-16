import json
import pytest
import requests
from unittest.mock import patch, Mock
from src import git
from src import llama


llama_url = "http://localhost:11434/api/generate"

def test_suggest_commit_messages_success():
    diff = "some diff text"
    mock_commit_text = (
        '1. "Refactor the user authentication process to improve security."\n'
        '2. "Update the README file with the latest installation instructions."\n'
        '3. "Fix the issue causing the app to crash on startup."\n'
        '4. "Optimize the database queries to reduce load times."'
    )

    with patch('requests.post') as mock_post:
        mock_response = Mock()
        mock_response.json.return_value = {"response": mock_commit_text}
        mock_post.return_value = mock_response

        result = llama.suggest_commit_messages(diff)

        expected_result = [
            "Refactor the user authentication process to improve security.",
            "Update the README file with the latest installation instructions.",
            "Fix the issue causing the app to crash on startup.",
            "Optimize the database queries to reduce load times."
        ]

        assert result == expected_result
        mock_post.assert_called_once_with(
            llama_url,
            headers={"content-type": "application/json"},
            data=json.dumps({
                "model": "llama3.1:latest",
                "prompt": llama.prepare_prompt(diff),
                "stream": False
            })
        )

def test_suggest_commit_messages_error():
    diff = "some diff text"

    with patch('requests.post', side_effect=Exception("Network error")) as mock_post:
        result = llama.suggest_commit_messages(diff)

        assert result == "Error while sending request to ollama! Network error"
        mock_post.assert_called_once_with(
            llama_url,
            headers={"content-type": "application/json"},
            data=json.dumps({
                "model": "llama3.1:latest",
                "prompt": llama.prepare_prompt(diff),
                "stream": False
            })
        )
