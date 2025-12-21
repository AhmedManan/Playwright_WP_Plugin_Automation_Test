import re
from playwright.sync_api import Page, expect
from utils.environment import base_url

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/cart'

        # Locators
        self.proceed_to_checkout_button = page.get_by_role("link", name="Proceed to Checkout")
        # self.cart_total_locator = page.locator('//span[contains(@class, "wc-block-components-totals-footer-item-tax-value")]')
        self.cart_total_locator = page.locator("#post-8")

        self.expected_total = 3461.85  # Example value

    def goto(self):
        self.page.goto(base_url+self.page_url)

    def proceed_to_checkout(self):
        expect(self.proceed_to_checkout_button).to_be_visible()
        self.proceed_to_checkout_button.click()

    def verify_cart_total_amount(self):
        expect(self.cart_total_locator).to_contain_text(f"{self.expected_total}৳")


