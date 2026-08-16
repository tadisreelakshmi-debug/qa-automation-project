import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(re.compile(".*inventory.html"))
    expect(inventory_page.page_title).to_have_text("Products")

def test_invalid_login_shows_error(page: Page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("locked_out_user", "wrong_password")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username and password do not match")

def test_add_item_to_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.go_to_cart()
    expect(page).to_have_url(re.compile(".*cart.html"))
    expect(inventory_page.cart_item_name).to_have_text("Sauce Labs Backpack")