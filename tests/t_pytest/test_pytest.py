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


# Mock
import os


class UnixFS:
    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    mocker.patch("os.remove")
    UnixFS.rm("file")
    os.remove.assert_called_once_with("file")


# Spy
# The mocker.spy object acts exactly like the original method in all cases, except
# the spy also tracks function/method calls, return values and exceptions raised.
# spy_exception
# unlike patch,
# spy acts exactly like the original method in all cases, except
# the spy also tracks function/method calls, return values and exceptions raised.
def test_spy_method(mocker):
    class Foo(object):
        def bar(self, v):
            return v * 2

    foo = Foo()
    spy = mocker.spy(foo, "bar")
    assert foo.bar(21) == 42

    spy.assert_called_once_with(21)
    assert spy.spy_return == 42


class Summ:
    @staticmethod
    def myfunction():
        return 42


def test_spy_function(mocker):
    spy = mocker.spy(Summ, "myfunction")
    assert Summ.myfunction() == 42
    assert spy.call_count == 1


# Stops Spying
def test_with_unspy(mocker):
    class Foo:
        def bar(self):
            return 42

    spy = mocker.spy(Foo, "bar")
    foo = Foo()
    assert foo.bar() == 42
    assert spy.call_count == 1
    mocker.stop(spy)
    assert foo.bar() == 42

    # call_count did not increase after stop()
    assert spy.call_count == 1


# Stub
# it accepts any args and is useful to test callbacks
def test_stub(mocker):
    def foo(on_something):
        on_something("foo", "bar")

    stub = mocker.stub(name="on_something_stub")
    foo(stub)
    stub.assert_called_once_with("foo", "bar")
