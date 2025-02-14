from playwright.sync_api import Page, expect

def test_playwithdata(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # Table Data Handling Generaically
    for index in range(page.locator("th").count()):  # Loop through all table headers
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColValue = index  # Store the index of the "Price" column
            print(f"Price column value is {priceColValue} ")
            break  # Stop after finding the first match
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")

