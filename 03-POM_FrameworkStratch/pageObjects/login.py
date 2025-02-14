from playwright.sync_api import expect


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def enter_valid_credentails_to_login(self, username, password):
        self.browser.get_by_role("textbox", name="Email").fill(username)
        self.browser.get_by_role("textbox", name="Password").fill(password)
        self.browser.get_by_role("button", name="Sign In").click()
        expect(self.browser.locator(".page-title")).to_have_text("Home Page")

    def click_on_logout_button(self):
        self.browser.locator("div[class='panel header'] span[role='button']").click()
        self.browser.get_by_role("link", name="Sign Out").click()
        expect(self.browser.locator(".page-title")).to_have_text("You are signed out")