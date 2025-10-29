# tests/test_streak.py
import pytest
from streak import longest_positive_streak

def test_basic_streak():
    assert longest_positive_streak([1, 2, 3, -1, 4, 5]) == 3

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_no_positive():
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5
