import pytest


def test_first(access_return_value):
    print("test case 01")
    assert access_return_value == "true"
@pytest.mark.smoke
def test_second(access_return_value):
    print("test case 02")
    assert access_return_value == "true"

@pytest.mark.skip
def test_third(access_return_value):
    print("test case 03")
    assert access_return_value == "true"

# if you want to run particularly 1 test case how you will run?
# sytanx : pytest <filename>::<testcase_name>

# say for example you want to run all the tcs except 3 rd / 1st / 2nd
# just use the @pytest.mark.skip            # we are marking here as skip, we are not using fixture, but we are using skip mark

# if you want to run only smoke test cases out of all test cases
# there is a concept called tagging
# @pytest.mark.smoke annotation should be used on test cases level that you want to make as part of smoke test cases
