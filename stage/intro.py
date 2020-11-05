"""
Copyright to 000010023 by WIUT student
"""

from .decorator import separators, welcome_text

welcome_time: bool = True

intro_text: str = "Welcome to my tutorial application by 10023 \n" \
                  "In this application I'll be introducing \n" \
                  "basic concepts of lists, tuples, dictionary \n" \
                  "and some functions as ... \n"

all_text: list[str] = [
    separators + welcome_text + separators,
    separators + intro_text + separators
]


def intro():
    global welcome_time
    if welcome_time is True:
        for texter in all_text:
            print(texter)
        welcome_time = False
    else:
        pass
