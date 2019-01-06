import pytest


def test_travis_fail():
    pytest.fail()


def test_travis_succeed():
    pass
