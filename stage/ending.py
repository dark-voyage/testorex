"""
Copyright to 000010023 by WIUT student
"""

from .decorator import separators, bye_text

welcome_time: bool = True

text: str = "Thanks for using my application, hope we \n" \
            "will see each other soon again! 00010023 \n"

all_texts: [str] = [
    separators + bye_text + text + separators
]


def ending():
    for texter in all_texts:
        print(texter)
    exit()
