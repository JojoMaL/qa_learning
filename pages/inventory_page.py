from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        self.products = page.locator(".inventory_item")

    def add_product_to_cart(self, product_name: str):
        self.products.filter(
            has_text=product_name
        ).get_by_role(
            "button", name="Add to cart"
        ).click()