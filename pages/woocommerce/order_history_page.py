from playwright.sync_api import Page, expect
from utils.environment import base_url


class OrderHistoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/my-account/orders'

        # Improved Locators
        self.view_order_details_button = page.get_by_role("link", name="View").first
        # Target the specific cell to avoid header text or hidden elements
        self.product_cells = page.locator("td.woocommerce-table__product-name")
        self.order_details_title = page.locator('.woocommerce-order-details__title')

    def goto(self):
        self.page.goto(base_url + self.page_url)

    def view_order_details(self):
        self.view_order_details_button.click()
        # ASSERTION: Ensure we are actually on the details page before proceeding
        expect(self.order_details_title).to_be_visible(timeout=10000)

    def get_all_products_in_order(self):
        # 1. CRITICAL: Wait for at least one product cell to be visible
        # This prevents all_text_contents() from returning [] too early.
        self.product_cells.first.wait_for(state="visible")

        # 2. Get all contents
        raw_names = self.product_cells.all_text_contents()

        product_names_list = []
        for name in raw_names:
            # Cleaning logic
            # WooCommerce often adds '× 1' or quantity strings inside the text content
            cleaned_name = name.split('×')[0].strip()  # Splits at the '×' and takes the first part

            # Convert curly apostrophe to straight
            cleaned_name = cleaned_name.replace('’', "'")

            if cleaned_name and cleaned_name != 'Product':
                product_names_list.append(cleaned_name)

        print(f"\nFound Product Names: {product_names_list}")
        return product_names_list