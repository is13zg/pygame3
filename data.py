import sys, os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


SIZE = (640, 480)
BAR = False
BJ = False
DESTROYED = False
JK = 8
DEATH = False
