from playwright.sync_api import Page, expect


def test_frame(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    #Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name='Top').click()


    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")
