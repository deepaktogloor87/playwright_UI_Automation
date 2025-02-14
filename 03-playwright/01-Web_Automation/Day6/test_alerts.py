import time

from playwright.sync_api import Page, expect

def test_Alerts(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on('dialog', lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()

