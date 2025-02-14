from playwright.sync_api import expect


class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to_homepage(self):
        self.browser.goto("https://magento.softwaretestingboard.com/")

    def click_create_an_account(self):
        self.browser.get_by_role("link", name="Create an Account").click()

    def click_sign_in(self):
        self.browser.get_by_role("link", name="Sign In").click()
        expect(self.browser.locator(".page-title")).to_have_text("Customer Login")

