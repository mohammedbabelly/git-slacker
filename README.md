# Git-Slacker
A simple Python script that uses the Llama3 API to generate commit messages based on a provided Git diff.

**Features:**

* Generates four clear and concise commit messages for a given Git diff
* Allows user to choose their preferred commit message


**Requirements:**

* Python 3.x
* OllAma running on `http://localhost:11434`
* `requests` library (`pip install requests`)

**Usage:**

1. Install the required dependencies by running `pip install requests`
2. Run the script with a Git diff as an argument, e.g., `python src/app.py </repo/path>`
3. If no argument is provided, you will be prompted to enter one manually
4. Choose your preferred commit message from the generated list to apply it