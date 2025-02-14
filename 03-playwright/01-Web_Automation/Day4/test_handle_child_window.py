def test_handle_child_window(playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as page_info:                       # child window should be wrapped in expect_popup recate object page_info
        page.locator(".blinkingText").click()
        documents_request = page_info.value
        myText = documents_request.locator(".red").text_content()       #grab text
        words = myText.split("at")
        email = (words[1]).strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"

