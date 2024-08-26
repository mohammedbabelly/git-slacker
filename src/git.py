import subprocess


def get_diff(repo_path: str):
    subprocess.run("git add .", shell=True, cwd=repo_path)

    output = subprocess.run(
        "git diff --staged",
        shell=True,
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return (
        output.stdout.decode("utf-8")
        if output.returncode == 0
        else output.stderr.decode("utf-8")
    )


def apply_commit(repo_path: str, commit_message: str):
    if commit_message:
        subprocess.run(
            f'git commit -m {commit_message}',
            shell=True,
            cwd=repo_path,
        )
        print(f"Commit ({commit_message}) applyed.")
