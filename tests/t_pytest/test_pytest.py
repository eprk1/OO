"""
$ pytest tests/
$ pytest tests/test_sample.py
$ pytest tests/test_sample.py::test_function_one

- All unit tests must be written in a tests/ directory
- File names should strictly start with test_
    Otherwise, pytest wont find the test file
- Function names should strictly start with test

pytest
pytest-mock
"""
import pytest
import sys


def test_function_with_scenario_one():
    print("Testing function with scenario one")
    assert 1 + 1 == 2, f"Check addition value {1 + 1} does not match {2}"


### Parameters
@pytest.mark.parametrize("n", [2, 4, 6])
def test_even_number(n):
    assert not n % 2, f"{n} is not an even number"


### Skip


@pytest.mark.skip
def test_skip():
    raise Exception("This test should be skipped")


@pytest.mark.skipif(sys.version_info.major == 2, reason="requires Python 3.x")
def test_skipif():
    pass


### Fail test
@pytest.mark.xfail
def test_fail():
    assert 1 == 2, "This should fail"


### pytest -m <group-name>
@pytest.mark.group1
def test_sample():
    print("test sample")


import os


class UnixFS:
    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    mocker.patch("os.remove")
    UnixFS.rm("file")
    os.remove.assert_called_once_with("file")
