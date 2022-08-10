from time import sleep
from random import randint


def random_sleep(start: int = 2, end: int = 4) -> int:
    """Random sleep time.

    Args:
        start (int, optional): range start. Defaults to 2.
        end (int, optional): range end. Defaults to 4.

    Returns:
        int: random int
    """
    return sleep(randint(start, end))
