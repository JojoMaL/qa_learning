from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.first_name = page.get_by_label("First Name")
        self.last_name = page.get_by_label("Last Name")
        self.zip_code = page.get_by_label("Zip/Postal Code")

    def fill_checkout_data(
        self,
        first_name: str,
        last_name: str,
        zip_code: str,
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_code.fill(zip_code)

    def continue_to_overview(self):
        self.page.get_by_role("button", name="Continue").click()

    def finish_purchase(self):
        self.page.get_by_role("button", name="Finish").click()