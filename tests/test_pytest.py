"""
$ pytest tests/
$ pytest tests/test_sample.py
$ pytest tests/test_sample.py::test_function_one

- All unit tests must be written in a tests/ directory
- File names should strictly start with test_
    Otherwise, pytest wont find the test file
- Function names should strictly start with test
"""


def test_function_with_scenario_one():
    print("Testing function with scenario one")
    assert 1 + 1 == 2, f"Check addition value {1 + 1} does not match {2}"
