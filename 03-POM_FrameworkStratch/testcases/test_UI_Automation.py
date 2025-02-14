import json
import time

import pytest
from playwright.sync_api import expect
from pageObjects.homePage import HomePage
from pageObjects.customerAccountCreate import CreateNewCustomerAccount
from pageObjects.login import LoginPage
from pageObjects.catalogSearch import ProductPage
from pageObjects.checkout import CheckoutPage

with open("../testdata/creds.json") as f:
    test_data = json.load(f)
    user_data = test_data["user_details"]


@pytest.mark.skip(reason="Skipping this test temporarily")
def test_Create_An_Account(playwright):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    homepage = HomePage(browser)
    homepage.navigate_to_homepage()
    homepage.click_create_an_account()
    cus_create_acc_page = CreateNewCustomerAccount(browser)
    cus_create_acc_page.enter_personal_details(user_data["firstname"], user_data["lastname"])
    cus_create_acc_page.enter_sign_in_information(user_data["email"], user_data["password"], user_data["password"])
    cus_create_acc_page.click_create_an_account()


@pytest.mark.parametrize('user_data', user_data)
def test_Create_An_Account_Existing_EmailId(playwright, user_data):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    homepage = HomePage(browser)
    homepage.navigate_to_homepage()
    homepage.click_create_an_account()
    cus_create_acc_page = CreateNewCustomerAccount(browser)
    cus_create_acc_page.enter_personal_details(user_data["firstname"], user_data["lastname"])
    cus_create_acc_page.enter_sign_in_information(user_data["email"], user_data["password"], user_data["password"])
    cus_create_acc_page.click_create_an_account()
    cus_create_acc_page.verify_user_already_exists_error_message()


@pytest.mark.parametrize('user_data', user_data)
def test_SignIn(playwright, user_data):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    homepage = HomePage(browser)
    homepage.navigate_to_homepage()
    homepage.click_sign_in()
    loginpage = LoginPage(browser)
    loginpage.enter_valid_credentails_to_login(user_data["email"], user_data["password"])
    loginpage.click_on_logout_button()


@pytest.mark.parametrize('user_data', user_data)
def test_Search_For_A_Product(playwright, user_data):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    homepage = HomePage(browser)
    homepage.navigate_to_homepage()
    homepage.click_sign_in()
    loginpage = LoginPage(browser)
    loginpage.enter_valid_credentails_to_login(user_data["email"], user_data["password"])
    productpage = ProductPage(browser)
    ActualProductName = productpage.search_product("jacket")
    assert ActualProductName == "Adrienne Trek Jacket"


@pytest.mark.parametrize('user_data', user_data)
def test_Product_Add_To_Cart(playwright, user_data):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    homepage = HomePage(browser)
    homepage.navigate_to_homepage()
    homepage.click_sign_in()
    loginpage = LoginPage(browser)
    loginpage.enter_valid_credentails_to_login(user_data["email"], user_data["password"])
    productpage = ProductPage(browser)
    # Select the "shirt for men" option
    productpage.search_product("shirt for men")
    successMessage = productpage.add_product_to_the_cart("Chloe Compete Tank")
    assert successMessage == "You added Chloe Compete Tank to your shopping cart."


@pytest.mark.parametrize('user_data', user_data)
def test_checkout_placeOrder(playwright, user_data):
    browser = playwright.chromium.launch(headless=False).new_context().new_page()
    homepage = HomePage(browser)
    homepage.navigate_to_homepage()
    homepage.click_sign_in()
    loginpage = LoginPage(browser)
    loginpage.enter_valid_credentails_to_login(user_data["email"], user_data["password"])
    productpage = ProductPage(browser)

    # Select the "shirt for men" option
    productpage.search_product("shirt for men")
    successMessage = productpage.add_product_to_the_cart("Chloe Compete Tank")
    assert successMessage == "You added Chloe Compete Tank to your shopping cart."

    # checkout
    checkoutpage = CheckoutPage(browser)
    checkoutpage.click_on_proceed_to_checkout()

    # shipping address
    # browser.get_by_role("textbox", name="Email Address").fill(user_data["email"])
    browser.get_by_role("textbox", name="First Name").fill(user_data["firstname"])
    browser.get_by_role("textbox", name="Last Name").fill(user_data["lastname"])
    browser.get_by_role("textbox", name="Company     ").fill(user_data["company"])
    browser.get_by_role("textbox", name="Street Address: Line 1").fill(user_data["streetAddress"])
    browser.get_by_role("textbox", name="City").fill(user_data["city"])
    browser.wait_for_selector("combobox", name="State").select_option(user_data["state"])
    browser.get_by_role("textbox", name="Zip/Postal Code").fill(user_data["zipCode"])
    browser.get_by_role("combobox", name="Country").select_option(user_data["country"])
    browser.get_by_role("textbox", name="Phone Number").fill(user_data["phone"])
    browser.get_by_role("radio", name="flatrate").click()
    browser.get_by_role("button", name="Next").click()

    # # payment method
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
