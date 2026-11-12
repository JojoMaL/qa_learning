import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def logged_page(page):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    return page



@pytest.mark.parametrize("checkout_data", [
    {
        "first_name": "Jose",
        "last_name": "Mantecon",
        "zip_code": "97000",
    },
    {
        "first_name": "Carlos",
        "last_name": "Test",
        "zip_code": "97100",
    },
])

@pytest.mark.playwright
def test_complete_purchase(logged_page, checkout_data):
    expect(logged_page.get_by_text("Products")).to_be_visible()

    inventory_page = InventoryPage(logged_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    print(logged_page.get_by_role("button").all_inner_texts())

    cart_page = CartPage(logged_page)
    cart_page.open_cart()

    expect(logged_page.get_by_text("Sauce Labs Backpack")).to_be_visible()

    cart_page.proceed_to_checkout()

    expect(logged_page.get_by_text("Checkout: Your Information")).to_be_visible()

    checkout_page = CheckoutPage(logged_page)
    checkout_page.fill_checkout_data(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["zip_code"],
    )

    expect(logged_page.get_by_label("First Name")).to_have_value(
        checkout_data["first_name"]
    )
    expect(logged_page.get_by_label("Last Name")).to_have_value(
        checkout_data["last_name"]
    )
    expect(logged_page.get_by_label("Zip/Postal Code")).to_have_value(
        checkout_data["zip_code"]
    )

    checkout_page.continue_to_overview()

    expect(logged_page.get_by_text("Checkout: Overview")).to_be_visible()
    expect(logged_page.get_by_text("Sauce Labs Backpack")).to_be_visible()

    checkout_page.finish_purchase()

    expect(
        logged_page.get_by_text("Thank you for your order!")
    ).to_contain_text("Thank you for your order!")



@pytest.mark.playwright
def test_homepage_error(page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    page.get_by_label("Username").fill("User")
    page.get_by_label("Password").fill("XXX")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Username and password do not match any user in this service")).to_be_visible()
    
    
   



@pytest.mark.parametrize("username,password,expected,expected_message", [
    ("standard_user", "secret_sauce", "success", ""),
    ("locked_out_user", "secret_sauce", "error", "Epic sadface: Sorry, this user has been locked out."),
    ("usuario_invalido", "password", "error", "Epic sadface: Username and password do not match any user in this service"),
])

@pytest.mark.smoke
@pytest.mark.playwright
def test_login(page, username, password, expected, expected_message):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

    login_page = LoginPage(page)
    login_page.login(username, password)

    if expected == "success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.get_by_text("Products")).to_be_visible()
    else:
        expect(page.get_by_text(expected_message)).to_be_visible()


@pytest.mark.playwright
def test_login_button_state(page):
    page.goto("https://www.saucedemo.com/")

    expect(page.get_by_role("button", name="Login")).to_be_enabled()

@pytest.mark.playwright
def test_playwright_waits_for_element(page):
    page.goto("https://www.saucedemo.com/")

    expect(page.get_by_role("textbox", name="Username")).to_be_visible()


@pytest.mark.playwright
def test_playwright_auto_waits_on_action(page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text(
        "Epic sadface: Username is required"
    )).to_be_visible()