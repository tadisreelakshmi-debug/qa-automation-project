from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator(".title")
        self.backpack_add_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_item_name = page.locator(".inventory_item_name")

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def go_to_cart(self):
        self.cart_link.click()