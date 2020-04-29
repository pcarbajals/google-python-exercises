#!/usr/bin/python3 -tt
import pytest
from src.basic.wordcount import print_words


@pytest.fixture
def expected_small_file_output():
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
coach 1
'''


@pytest.fixture
def expected_simple_file_output():
    return '''to 2
be, 1
or 1
not 1
be 1
-- 1
william 1
shakespeare 1
'''


def test_print_words_with_small_file(capsys, expected_small_file_output):
    print_words('tests/small.txt')
    assert capsys.readouterr().out == expected_small_file_output


def test_print_words_with_simple_file(capsys, expected_simple_file_output):
    print_words('tests/simple.txt')
    assert capsys.readouterr().out == expected_simple_file_output
