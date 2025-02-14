from playwright.sync_api import Playwright

def test_healthCheck(playwright:Playwright):
    request = playwright.request.new_context(base_url="https://practice.expandtesting.com")
    response = request.get(url="/notes/api/health-check",
                           headers={"content-type": "application/json"})
    #Verify Response Status
    assert response.status == 200
    JsonBody = response.json()
    assert JsonBody["success"]==True
    assert JsonBody["status"]==200
    assert JsonBody["message"]=="Notes API is Running"

def test_userRegister(playwright:Playwright):
    request = playwright.request.new_context(base_url="https://practice.expandtesting.com")
    response = request.post(url="/notes/api/users/register",
                           headers={"content-type": "application/x-www-form-urlencoded",
                                    "accept":"application/json"},
                           data='name=deepak11&email=deepak%40deepak1.com&password=deepak')
    responseBody = response.json()
    assert (responseBody)["message"]=="An account already exists with the same email address"

def test_userLogin(playwright:Playwright):
    request = playwright.request.new_context(base_url="https://practice.expandtesting.com")
    creds = {
        "email": "deepak@deepak1.com",
        "password": "deepak"
        }
    response = request.post(url="/notes/users/login",
                            headers={"content-type":"application/json",
                                     "accept":"application/json"},
                            data=creds)
    bodyResponse = response.json()
    bodyResponse = response.json()
    print(bodyResponse)
