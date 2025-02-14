import playwright
from playwright.sync_api import expect

# def test_login_creds(page):
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
#     page.get_by_role("textbox",name="username").fill("rahulshettyacademy")
#     page.get_by_label("Password:").fill("learning132")
#     page.get_by_role("radio",name=" User").click()
#     page.get_by_role("button",name="Okay").click()
#     page.get_by_role("combobox").select_option("teach")
#     page.get_by_role("link",name="terms and conditions").click()
#     page.locator("#terms").click()
#     page.get_by_role("button",name="Sign In").click()
#
#     #Assertion
#     # grab text from the page use : get_by_text       and  to_be_visible
#     expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


def test_login_creds_wit_firefox(playwright):
    # page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # we have to use custamized engine driver to run on firefox
    # firefoxbrowser = playwright.firefox.launch(headless=False)
    # context = firefoxbrowser.new_context()
    # page = context.new_page()
    page = playwright.firefox.launch(headless=False).new_context().new_page()       # in single line
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox",name="username").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning132")
    page.get_by_role("radio",name=" User").click()
    page.get_by_role("button",name="Okay").click()
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link",name="terms and conditions").click()
    page.locator("#terms").click()
    page.get_by_role("button",name="Sign In").click()

    #Assertion
    # grab text from the page use : get_by_text       and  to_be_visible
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()