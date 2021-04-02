from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators, BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_THE_BASKET), \
            "Some products in the basket, should be empty"

    def should_be_empty_basket_massage(self):
        emty_msg = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG).text
        assert bool(emty_msg), "No message regarding basket is empty"