"""Auto Commit Name Generator: Generates a unique git commit name based on the changes made to a repository"""
import os
import subprocess
import sys
from pathlib import Path

from chatgpt_wrapper import ChatGPT


def main() -> int:
    args = sys.argv[1:]

    if not args:
        project_path = Path("./").absolute()
    else:
        project_path = Path(args[0]).absolute()

    os.chdir(str(project_path))

    output = subprocess.run(
        ["git", "diff", "HEAD"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert not output.stderr, "Error occurred when trying to get git difference"

    assert output.stdout, "No output was provided."

    chatgpt = ChatGPT()

    response = chatgpt.ask(
        f"Generate a git commit message/name mentioning all the changes from the following data:\n\n{output.stdout.decode()}"
    )

    print(response)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
