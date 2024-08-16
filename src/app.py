import llama
import git
import sys


def select_one_commit_message(messages) -> str:
    print(
        f"Here are the suggestions, please enter the number of the commit message you wish to use or -1 to exit."
    )

    for i, msg in enumerate(messages[:4]):
        print(f"{i+1}. {msg}")

    while True:
        choice = input("\n")

        if choice == "-1":
            exit()
        elif choice.isdigit() and 1 <= int(choice) <= 4:
            return messages[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def main():
    repo_path = repo_path = (
        sys.argv[1]
        if len(sys.argv) >= 2
        else input("No repo path provided. Enter your git repo path...\n")
    )

    diff = git.get_diff(repo_path)

    messages = llama.suggest_commit_messages(diff)
    commit_message = select_one_commit_message(messages)

    if commit_message:
        git.apply_commit(repo_path, commit_message)


if __name__ == "__main__":
    main()
