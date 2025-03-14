# test_math_module.py

import pytest
from math_module import addition, soustraction, multiplication

def test_addition():
    assert addition(2, 3) == 5

def test_soustraction():
    assert soustraction(5, 3) == 2


def test_multiplication():
    assert multiplication(2, 3) == 6


