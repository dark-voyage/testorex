"""
Copyright to 000010023 by WIUT student
"""

from .intro import intro
from .menu import menu

functions: list[any] = [
    intro, menu
]


def launcher():
    for function in functions:
        function()
    pass
