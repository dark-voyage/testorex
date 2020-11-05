"""
Copyright to 000010023 by WIUT student
"""

import colorly


def test_colorly():
    for color in vars(colorly.Colorly):
        assert type(color) == str
