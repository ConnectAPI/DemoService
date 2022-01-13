from fastapi import APIRouter

from api.random import random_from_range, secure_random_string

random_router = APIRouter(prefix="/random", tags=["random"])


@random_router.get("/range")
def random_int_from_range(a: int, b: int) -> int:
    """returns random number between a and b"""
    return random_from_range(start=a, end=b)


@random_router.get("/string")
def random_string(n: int) -> str:
    """returns random string of length n created securely"""
    return secure_random_string(n)
