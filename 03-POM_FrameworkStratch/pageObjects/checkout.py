class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser

    def click_on_proceed_to_checkout(self):
        self.browser.get_by_role("link", name="shopping cart").click()
        self.browser.wait_for_selector("button[title='Proceed to Checkout'] span").click()