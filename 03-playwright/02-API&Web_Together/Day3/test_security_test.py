import time

from playwright.sync_api import Page

def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_network_mock(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("email.123@example.com")
    page.get_by_placeholder("enter your passsword").fill("Email@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="  ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    page.locator(".blink_me").filter(has_text="You are not authorize to view this order")
