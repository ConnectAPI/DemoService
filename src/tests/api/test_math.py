from api.math import sum, mul


def test_sum():
    assert sum(5, 3) == 8


def test_mul():
    assert mul(5, 7) == 35
