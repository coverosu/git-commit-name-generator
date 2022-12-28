"""Auto Commit Name Generator: Generates a unique git commit name based on the changes made to a repository"""
import subprocess

from chatgpt_wrapper import ChatGPT


def main() -> int:

    output = subprocess.run(
        ["git", "diff"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert not output.stderr, "Error occurred when trying to get git difference"

    chatgpt = ChatGPT()

    commit_name = chatgpt.ask(
        f"Generate a git commit message/name mentioning all the changes from the following data:\n\n{output.stdout.decode()}"
    )

    print(commit_name)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
