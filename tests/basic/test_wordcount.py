#!/usr/bin/python3 -tt
import pytest
from src.basic.wordcount import print_words
from src.basic.wordcount import print_top


@pytest.fixture
def print_words_small_output():
    return '''-- 1
are 3
at 1
be 3
but 1
coach 1
football 1
least 1
need 1
not 3
should 1
to 2
used 1
we 6
what 3
'''


@pytest.fixture
def print_words_simple_output():
    return '''-- 1
be 1
be, 1
not 1
or 1
shakespeare 1
to 2
william 1
'''



@pytest.fixture
def print_top_small_output():
    return '''we
are
not
what
be
to
should
need
but
at
least
used
--
football
coach
'''



@pytest.fixture
def print_top_large_output():
    return '''the
and
to
a
she
of
said
it
in
was
you
i
as
that
alice
her
at
had
with
all
'''


def test_print_words_with_small_file(capsys, print_words_small_output):
    print_words('tests/small.txt')
    assert capsys.readouterr().out == print_words_small_output


def test_print_words_with_simple_file(capsys, print_words_simple_output):
    print_words('tests/simple.txt')
    assert capsys.readouterr().out == print_words_simple_output


def test_print_top_with_small_file(capsys, print_top_small_output):
    print_top('tests/small.txt')
    assert capsys.readouterr().out == print_top_small_output


def test_print_top_with_large_file(capsys, print_top_large_output):
    print_top('tests/alice.txt')
    assert capsys.readouterr().out == print_top_large_output
