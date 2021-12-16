from secrets import token_urlsafe
from random import randrange


def random_from_range(start: int, end: int) -> int:
    return randrange(start, end)


def secure_random_string(length: int) -> str:
    return token_urlsafe(length)[:length]
