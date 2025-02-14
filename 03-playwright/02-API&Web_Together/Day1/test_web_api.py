import time

from playwright.sync_api import Playwright, expect
from test_API import APIUtils

def test_e2e_web_api(playwright:Playwright):
    # create order using web apis
    api_utils = APIUtils()
    api_order_id = api_utils.crate_order(playwright)
    #login
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("email.123@example.com")
    page.get_by_placeholder("enter your passsword").fill("Email@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="  ORDERS").click()
    row = page.locator("tr").filter(has_text=api_order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
