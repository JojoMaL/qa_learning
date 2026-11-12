import re

from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_button = page.get_by_role(
            "button",
            name=re.compile("^Cart")
        )

    def open_cart(self):
        self.cart_button.click()

    def proceed_to_checkout(self):
        self.page.get_by_role("button", name="Checkout").click()