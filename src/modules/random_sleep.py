from time import sleep
from random import randint


def random_sleep(start: int = 2, end: int = 4) -> int:
    return sleep(randint(start, end))
