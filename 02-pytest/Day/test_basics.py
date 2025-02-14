# as well all understood how to write a functions in our 01-python class
import pytest


# def test_sample():
#     print("hello world")
#
# test_sample()

# but with respect to 02-pytest has some rule i.e
# a file name must be begin / end with test_ / _test.py
# also the function name must be begin with test_

#lets create a sample files and see practically
# a single file can contain multiple functions

# to run the tests we have different methods
# you can directly click on the green button to run the tests / on the terminal type 02-pytest to run the tests


# assume that now you have 10 test cases already written and in 10 tcs you have to open the browser on each tc level
# and close the browser on each tc level
# to avoid this we can use fixtures to avoid this

# lets create a fixture

# to create a fixture we have to use the @02-pytest.fixture decorator
# what is decorator we have already seen in our 01-python class.
# those who miss the session or someone not aware highly recommend you to go to the 01-python class playlist
# still any confiusion will clarify in our test class

# lets create a fixture
@pytest.fixture
def brwoser_open_close():               # as you can see we have not given test name to the fixture it means its a function not a test case
    print("open the browser")
    yield
    print("close the browser")

def test_case01():
    print("test case 01")               #but we want before executing this tc browser should be open and after execution it should be closed

# to link it with test case simply pass the function name as argument in it
# def test_case01(brwoser_open_close):
#     print("test case 01")

# this is just 1 simple example what else we have some use case where in our project requires other stuff also?
# we have another approach to do that is we can create another fixture file conftest.py and write all our fixtures init
# will see as we go on deep dive in our upcoming classes.

# fixture will come in different scopes
# 1. module scope
# 2. class scope
# 3. function scope

# module scope is a global scope
# class scope is a local scope
# function scope is a function scope
