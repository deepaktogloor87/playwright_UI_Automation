def test_validation(access_return_value):
    print("validating the return value")
    assert access_return_value == "fail"


#with that we have understood is how conftest.py file is plays important role
#and fixtures are not limited to test cases only we can return the value if we want and use it in our test cases
