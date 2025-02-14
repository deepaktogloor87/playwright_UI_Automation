# will understand and identify basic web component using getLabel and get_by_role methods
import time

from playwright.sync_api import sync_playwright
def test_login_creds(page):
    # It will navigate to the url
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    #Get the locator by label and fill method is type the username
    '''
    condition1 here is you cannot use get_by_label if <lable> tag is not present
    condition2 <label> should be embeded with the same tag
    '''
    # page.get_by_label("Username:").fill("rahulshettyacademy ")

    #other option would be get_by_role what type of locator you want and what is the name of the locator
    page.get_by_role("textbox",name="username").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")

    # if you are working on radio button select the radio button and name & method
    page.get_by_role("radio",name=" User").click()

    # if you are working on button select the radio and name & method
    page.get_by_role("button",name="Okay").click()

    # if you are working on combobox select the options name
    page.get_by_role("combobox").select_option("teach")

    # if you are working on links select the link and name & method
    page.get_by_role("link",name="terms and conditions").click()

    # if you are using css locators and page.locators shoud be used and if id then use #, if class then use .
    page.locator("#terms").click()
    page.get_by_role("button",name="Sign In").click()
    time.sleep(5)

