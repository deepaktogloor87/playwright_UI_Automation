import time

import playwright
import pytest
from playwright.sync_api import expect


@pytest.mark.skip(reason="Skipping this test temporarily")
def test_Create_An_Account(playwright):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    browser.goto("https://magento.softwaretestingboard.com/")
    browser.get_by_role("link", name="Create an Account").click()
    expect(browser.locator(".page-title")).to_have_text("Create New Customer Account")
    browser.get_by_role("textbox", name="First Name").fill("deepak")
    browser.get_by_role("textbox", name="Last Name").fill("togloor")
    browser.get_by_role("textbox", name="Email").fill("deepaktogloor123@gmail.com")
    browser.locator("input[name='password']#password").fill("Deepaktogloor@123")
    browser.locator("#password-confirmation").fill("Deepaktogloor@123")
    browser.get_by_role("button", name="Create an Account").click()
    expect(browser.locator(".page-title")).to_have_text("My Account")


def test_Create_An_Account_Existing_EmailId(playwright):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    browser.goto("https://magento.softwaretestingboard.com/")
    browser.get_by_role("link", name="Create an Account").click()
    expect(browser.locator(".page-title")).to_have_text("Create New Customer Account")
    browser.get_by_role("textbox", name="First Name").fill("deepak")
    browser.get_by_role("textbox", name="Last Name").fill("togloor")
    browser.get_by_role("textbox", name="Email").fill("deepaktogloor123@gmail.com")
    browser.locator("input[name='password']#password").fill("Deepaktogloor@123")
    browser.locator("#password-confirmation").fill("Deepaktogloor@123")
    browser.get_by_role("button", name="Create an Account").click()
    error_message = browser.inner_text(".message-error")
    expected_error_message = "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."
    assert error_message == expected_error_message


def test_SignIn(playwright):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    browser.goto("https://magento.softwaretestingboard.com/")
    browser.get_by_role("link", name="Sign In").click()
    expect(browser.locator(".page-title")).to_have_text("Customer Login")
    browser.get_by_role("textbox", name="Email").fill("deepaktogloor123@gmail.com")
    browser.get_by_role("textbox", name="Password").fill("Deepaktogloor@123")
    browser.get_by_role("button", name="Sign In").click()
    expect(browser.locator(".page-title")).to_have_text("Home Page")
    browser.locator("div[class='panel header'] span[role='button']").click()
    browser.get_by_role("link", name="Sign Out").click()
    expect(browser.locator(".page-title")).to_have_text("You are signed out")


def test_Search_For_A_Product(playwright):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    browser.goto("https://magento.softwaretestingboard.com/")
    browser.get_by_role("link", name="Sign In").click()
    expect(browser.locator(".page-title")).to_have_text("Customer Login")
    browser.get_by_role("textbox", name="Email").fill("deepaktogloor123@gmail.com")
    browser.get_by_role("textbox", name="Password").fill("Deepaktogloor@123")
    browser.get_by_role("button", name="Sign In").click()
    expect(browser.locator(".page-title")).to_have_text("Home Page")
    # Select the "shirt for men" option
    browser.locator("#search").fill(" Tanks")
    browser.keyboard.press("Enter")
    productName = browser.wait_for_selector(".product-item-name").inner_text()
    assert productName == "Typhon Performance Fleece-lined Jacket"

def test_Product_Add_To_Cart(playwright):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    browser.goto("https://magento.softwaretestingboard.com/")
    browser.get_by_role("link", name="Sign In").click()
    expect(browser.locator(".page-title")).to_have_text("Customer Login")
    browser.get_by_role("textbox", name="Email").fill("deepaktogloor123@gmail.com")
    browser.get_by_role("textbox", name="Password").fill("Deepaktogloor@123")
    browser.get_by_role("button", name="Sign In").click()
    expect(browser.locator(".page-title")).to_have_text("Home Page")
    # Select the "shirt for men" option
    browser.locator("#search").fill("jacket")
    browser.keyboard.press("Enter")
    product = browser.get_by_role("listitem").filter(has_text="Juno Jacket")
    size = product.get_by_label("XS")
    size.click()
    color = product.get_by_label("Blue")
    color.click()
    product.get_by_role("button", name="Add to Cart").click()
    successMessage = browser.inner_text("div.message-success")
    assert successMessage == "You added Juno Jacket to your shopping cart."

def test_checkout_placeOrder(playwright):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    browser.goto("https://magento.softwaretestingboard.com/")
    browser.get_by_role("link", name="Sign In").click()
    expect(browser.locator(".page-title")).to_have_text("Customer Login")
    browser.get_by_role("textbox", name="Email").fill("deepaktogloor123@gmail.com")
    browser.get_by_role("textbox", name="Password").fill("Deepaktogloor@123")
    browser.get_by_role("button", name="Sign In").click()
    expect(browser.locator(".page-title")).to_have_text("Home Page")
    # Select the "shirt for men" option
    browser.locator("#search").fill("jacket")
    browser.keyboard.press("Enter")
    product = browser.get_by_role("listitem").filter(has_text="Juno Jacket")
    size = product.get_by_label("XS")
    size.click()
    color = product.get_by_label("Blue")
    color.click()
    product.get_by_role("button", name="Add to Cart").click()
    successMessage = browser.inner_text("div.message-success")
    assert successMessage == "You added Juno Jacket to your shopping cart."

    # checkout
    browser.get_by_role("link", name="shopping cart").click()
    browser.get_by_role("button", name="Proceed to Checkout").click()
    #shipping address
    # browser.get_by_role("textbox", name="Email Address * Email Address").fill("deepaktogloor123@gmail.com")
    browser.get_by_role("textbox", name="First Name").fill("deepak")
    browser.get_by_role("textbox", name="Last Name").fill("togloor")
    browser.get_by_role("textbox", name="Company").fill("google company")
    browser.get_by_role("textbox", name="Street Address: Line 1").fill("google company")
    browser.get_by_role("textbox", name="City").fill("Anytown")
    browser.get_by_role("listbox").select_option("Virginia")
    browser.get_by_role("textbox", name="Zip/Postal Code").fill("456578")
    browser.get_by_role("listbox").select_option("Vatican City")
    browser.get_by_role("textbox", name="Phone Number").fill("9999999999")
    browser.get_by_role("radio", name="flatrate").click()
    browser.get_by_role("button", name="Next").click()

    #payment method
    checkbox = browser.get_by_role("checkbox", name="My billing and shipping")

    # Check if already checked
    if not checkbox.is_checked():
        checkbox.check()
        print("✅ Checkbox was unchecked. Now checked.")
    else:
        print("⚠️ Checkbox was already checked. Skipping.")

    browser.get_by_role("button", name="Place Order").click()
    OrderMessage = browser.locator("page-title").inner_text()
    assert OrderMessage == "Thank you for your purchase!"