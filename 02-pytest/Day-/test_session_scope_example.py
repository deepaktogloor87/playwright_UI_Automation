def test_session_scope1(open_close_browser):
    print("test case 01")

def test_session_scope2(open_close_browser):
    print("test case 02")


# what we are doing here is
#Step1: we need to create a conftest.py file and write fixture in that file
#Step2: create test file and write your test cases
# How it works i will tell you.
#   when you execute the file, it will first execute the conftest.py file and then execute the test file
#   so basically conftest file will be recognized globally ? correct.
#   and test file will be recognized locally, in local we have provided linkage of fixture (by name)
#   so it will check the fixture locally if it not found then next it will search for global file which is conftest

# this is very import **** will take a help of this concept while creating our framework.

