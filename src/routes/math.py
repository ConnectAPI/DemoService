from fastapi import APIRouter

from api.math import sum, mul

math_router = APIRouter(prefix="/math", tags=["math"])


@math_router.get("/sum")
def sum_two_numbers(a: int, b: int) -> int:
    """returns the sum of a and b"""
    return sum(a, b)


@math_router.get("/mul")
def multiply_two_numbers(a: int, b: int) -> int:
    """returns the product of a and b"""
    return mul(a, b)
