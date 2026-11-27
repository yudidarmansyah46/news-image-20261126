"""Entry for news-image-20261126.

Standard library only. It copies the front page drawn in advance
(entry.png, produced by draw.py in this repository) into the
grader's output folder, byte for byte, so repeated runs agree.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(target, "entry.png"))


if __name__ == "__main__":
    main()
