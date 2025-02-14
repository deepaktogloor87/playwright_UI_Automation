#===> a quick recap

'''fixture will come in different scopes
1. module scope
2. class scope
3. function scope

module scope is a global scope
class scope is a local scope
function scope is a function scope'''
import pytest


# @02-pytest.fixture(scope="function")                 # by default scope is function
# def open_close_browser:
#     print("open the browser")
#     yield "browser"
#     print("close the browser")
#
# def test_function_scope1(open_close_browser):
#     print("test case 01")
#
# def test_function_scope2(open_close_browser):
#     print("test case 02")

# @02-pytest.fixture(scope="module")                 # now scope is => module
# def open_close_browser():
#     print("open the browser")
#     yield "browser"
#     print("close the browser")
#
# def test_function_scope1(open_close_browser):
#     print("test case 01")
#
# def test_function_scope2(open_close_browser):
#     print("test case 02")

# did you guys see the difference, though even we linked the fixture with the test case its not opening and closing the browser
# with all the test cases, instead it just opened the browser once and closed it once

# now lets see the class scope
# the scope==> class is ==> scope==> module is same. only the difference is it is local to the class
# and we must have to have 1 class for each test cases

# @02-pytest.fixture(scope="class")
# def open_close_browser():
#     print("open the browser")
#     yield "browser"
#     print("close the browser")
#
# class TestClass:
#     def test_class_scope1(self, open_close_browser):
#         print("test case 01")
#
#     def test_class_scope2(self, open_close_browser):
#         print("test case 02")


######============ there is a one more scope which is session scope as i was mentioned in the video
#early stage about conftest.py (make sure the file name should be exactly the same and should be placed
#in the folder where your test cases are present to avoid encounter any errors.

# @02-pytest.fixture(scope="session")
# def open_close_browser():
#     print("open the browser")
#     yield "browser"
#     print("close the browser")
#
# def test_session_scope1(open_close_browser):
#     print("test case 01")
#
# def test_session_scope2(open_close_browser):
#     print("test case 02")
