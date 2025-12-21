import re
from pages.wordpress.admin_dashboard import AdminDashboard
from pages.wordpress.login_page import LoginPage
from pages.woocommerce.orders_page import OrdersPage
from pages.woocommerce.product_page import ProductPage
from pages.woocommerce.checkout_page import CheckoutPage
from pages.woocommerce.cart_page import CartPage
from utils.product_data_utils import get_csv_data
from playwright.sync_api import Page


class TestCheckoutFlow:

    expected_total_sum = 3041.85

    def test_check_out_flow(self, page: Page):
        # ------------------------------------
        """End-to-End Checkout Flow"""
        # ------------------------------------

        login_page = LoginPage(page)
        login_page.login()

        products_to_add = get_csv_data()

        for product in products_to_add:
            page_url_slug = product["page_url_slug"]

            print(f"Adding product: {page_url_slug} to cart...")

            product_page = ProductPage(page, page_url_slug)

            product_page.goto(page_url_slug)

            product_page.add_to_cart_button.click()


        cart_page = CartPage(page)
        cart_page.goto()
        page.wait_for_selector(".wc-block-components-totals-wrapper", state="visible", timeout=10000)
        # Expected value based on test data: item prices + tax + shipping

        # The actual value from the page
        # cart_page.verify_cart_total_amount()
        cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(page)
        # checkout_page.goto()
        checkout_page.contact_shipping_form()
        checkout_page.place_order()

        pattern = re.compile(r'https://zeushood.com/checkout/order-received/.*')
        page.wait_for_url(pattern)

        admin_dashboard = AdminDashboard(page)
        admin_dashboard.goto()
        orders_page = OrdersPage(page)
        orders_page.goto()
        orders_page.view_order()
        page.wait_for_timeout(5000)