"""
Copyright to 000010023 by WIUT student
"""


class Colorly:
    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE: str = '\033[4m'

    def __init__(self, text):
        self.text = text

    def bold(self):
        return self.BOLD + self.text + self.ENDC

    def error(self):
        return self.FAIL + self.text + self.ENDC

    def success(self):
        return self.OKGREEN + self.text + self.ENDC

    def warning(self):
        return self.WARNING + self.text + self.ENDC
