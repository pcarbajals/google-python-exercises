#!/usr/bin/python3 -tt
import pytest
from src.basic.wordcount import print_words


@pytest.fixture
def small_filename():
    return 'tests/small.txt'


def test_print_words(small_filename):
    assert print_words(small_filename) == small_filename
