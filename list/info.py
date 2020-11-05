"""
List Introductory

In this file I'll be coding about introductory basis
knowledge of lists on python.

Copyright to 000010023 by WIUT student
"""
example_list = ["green", 123456789, True, [], {}, ()]

information = \
    f"""
Lists on Python

List is a type of Python Collection where it's ordered
and any data containing python list can be changed or replaced!
Lists are appointed with curly brackets and it can contain strings,
numbers, another lists, tuples & dictionaries...

Let me show an example:
I'd like to assign "example = ["green", 123456789, True, [], ()]"
list and let's see result...
{example_list}
"""


def info():
    print(information)
    input("Continue? [Press Enter]")
    pass
