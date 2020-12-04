"""
Copyright to 000010023 by WIUT student
"""

from stage.intro import all_text
from stage.menu import menus


def test_intro_stage():
    for text in all_text:
        assert type(text) == str


def test_menu_stage():
    for obj in [menus]:
        assert type(obj) == dict
        for key in obj.keys():
            assert type(key) == int
