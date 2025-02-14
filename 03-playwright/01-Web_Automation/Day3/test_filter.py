import playwright
from playwright.sync_api import expect


def test_add_to_cart(playwright):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    browser.goto("https://rahulshettyacademy.com/loginpagePractise/")
    browser.get_by_role("textbox", name="username").fill("rahulshettyacademy")
    browser.get_by_role("textbox", name="password").fill("learning")
    browser.get_by_role("radio", name="Admin").click()
    browser.get_by_role("combobox").select_option("Teacher")
    browser.get_by_role("checkbox", name="terms").click()
    browser.get_by_role("button", name="Sign In").click()
    expect(browser.get_by_text("Shop Name")).to_be_visible()

    # add items to the cart dynamically
    browser.locator("app-card").filter(has_text="iphone X").get_by_role("button", name="Add").click()
    browser.locator("app-card").filter(has_text="Nokia Edge").get_by_role("button", name="Add").click()
    # click on checkout button
    browser.get_by_text("Checkout").click()
    # assertion to check the count of items added
    expect(browser.locator(".media-body")).to_have_count(2)
    # check the item name that we added are same only
    expect(browser.get_by_text("iphone X")).to_be_visible()
    expect(browser.get_by_text("Nokia Edge")).to_be_visible()



