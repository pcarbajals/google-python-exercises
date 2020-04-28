#!/usr/bin/python3 -tt
import pytest
from src.basic.wordcount import print_words


@pytest.fixture
def small_file_print_words():
    return '''we 6
are 3
not 3
what 3
should 1
be 3
need 1
to 2
but 1
at 1
least 1
used 1
-- 1
football 1
coach 1'''


def test_print_words(small_file_print_words):
    assert print_words('tests/small.txt') == small_file_print_words
