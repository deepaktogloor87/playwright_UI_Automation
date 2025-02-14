from playwright.sync_api import Playwright

fakeResponse = {"data":[],"message":"No Orders"}
def intercept_reponse(route):
    route.fulfill(
        json = fakeResponse
    )

def test_network_mock(playwright:Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_reponse)
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("email.123@example.com")
    page.get_by_placeholder("enter your passsword").fill("Email@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="  ORDERS").click()
    order_message = page.locator(".mt-4").text_content()
    print(order_message)
