import subprocess
from unittest.mock import patch

from src import git

def test_get_diff():
    repo_path = "/path/to/repo"
    
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git diff --staged"],
            returncode=0,
            stdout=b"mocked diff output",
            stderr=b""
        )
        
        result = git.get_diff(repo_path)
        
        mock_run.assert_any_call("git add .", shell=True, cwd=repo_path)
        mock_run.assert_any_call(
            "git diff --staged",
            shell=True,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        assert result == "mocked diff output"

def test_get_diff_with_error():
    repo_path = "/path/to/repo"
    
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git diff --staged"],
            returncode=1,
            stdout=b"",
            stderr=b"error message"
        )
        
        result = git.get_diff(repo_path)
        
        mock_run.assert_any_call("git add .", shell=True, cwd=repo_path)
        mock_run.assert_any_call(
            "git diff --staged",
            shell=True,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        assert result == "error message"
