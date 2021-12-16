from api.random import random_from_range, secure_random_string


def test_random_range():
    assert 0 <= random_from_range(0, 10) <= 10


def test_random_string():
    assert len(secure_random_string(10)) == 10
    assert secure_random_string(100) != secure_random_string(100)  # big enough
