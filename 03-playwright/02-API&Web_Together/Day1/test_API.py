from playwright.sync_api import Playwright, expect

class APIUtils:
    def get_token(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": "email.123@example.com", "userPassword": "Email@123"},
                                 headers={"content-type": "application/json"})
        assert response.ok
        responseBody=response.json()
        return responseBody["token"]

    def crate_order(self,playwright:Playwright):
        token = self.get_token(playwright)
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_req_context.post("/api/ecom/order/create-order",
                             data = {"orders": [{"country": "India", "productOrderedId": "6581cade9fd99c85e8ee7ff5"}]},
                             headers={"Authorization":token,
                                      "content-type":"application/json"},
                             )
        return response.json()["orders"]

