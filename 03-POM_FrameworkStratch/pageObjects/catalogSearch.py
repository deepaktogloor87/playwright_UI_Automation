class ProductPage:
    def __init__(self, browser):
        self.browser = browser

    def search_product(self, product_name):
        self.browser.locator("#search").fill(product_name)
        self.browser.keyboard.press("Enter")
        productName = self.browser.wait_for_selector(".product-item-name").inner_text()
        return productName

    def add_product_to_the_cart(self, productname):
        product = self.browser.get_by_role("listitem").filter(has_text=productname)
        size = product.get_by_label("XS")
        size.click()
        color = product.get_by_label("Blue")
        color.click()
        product.get_by_role("button", name="Add to Cart").click()
        successMessage = self.browser.inner_text("div.message-success")
        return successMessage