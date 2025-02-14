from playwright.sync_api import expect


class CreateNewCustomerAccount:
    def __init__(self, browser):
        self.browser = browser

    def click_create_an_account(self):
        self.browser.get_by_role("button", name="Create an Account").click()

    def enter_personal_details(self, firstname, lastname):
        expect(self.browser.locator(".page-title")).to_have_text("Create New Customer Account")
        self.browser.get_by_role("textbox", name="First Name").fill(firstname)
        self.browser.get_by_role("textbox", name="Last Name").fill(lastname)

    def enter_sign_in_information(self, email, password, confirm_password):
        self.browser.get_by_role("textbox", name="Email").fill(email)
        self.browser.locator("input[name='password']#password").fill(password)
        self.browser.locator("#password-confirmation").fill(confirm_password)

    def click_on_create_an_account(self):
        self.browser.get_by_role("button", name="Create an Account").click()
        expect(self.browser.locator(".page-title")).to_have_text("My Account")

    def verify_user_already_exists_error_message(self):
        error_message = self.browser.inner_text(".message-error")
        expected_error_message = "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."
        assert error_message == expected_error_message