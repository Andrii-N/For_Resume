from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_able_add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.should_be_product_price_info()
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_massages_regarding_product_in_the_basket()
        self.should_be_same_product_name_in_massage_and_selected_product_name()
        self.should_be_same_price_of_the_product_and_basket()


    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), \
            "Basket Button not presented or check Locator"

    def should_be_product_price_info(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), \
            "No price Info"

    def add_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    def should_be_massages_regarding_product_in_the_basket(self):
        assert \
            self.is_element_present(*ProductPageLocators.MASSAGE_OF_PRODUCT_FROM_THE_BASKET), \
            "No massages regarding product in the basket"

    def should_be_same_product_name_in_massage_and_selected_product_name(self):
        name_in_the_massage = \
            self.browser.find_element(*ProductPageLocators.MASSAGE_OF_PRODUCT_FROM_THE_BASKET).text
        name_of_the_product = self.browser.find_element(*ProductPageLocators.NAME_OF_THE_PRODUCT).text
        assert name_in_the_massage == name_of_the_product, \
            "Product name in the massage and selected product have different names"

    def should_be_same_price_of_the_product_and_basket(self):
        price_of_the_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_BASKET).text
        price_of_the_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT).text
        assert price_of_the_basket == price_of_the_product, \
            "Product Price not equal to Basket Price"

    def should_be_no_success_massage(self):
        assert self.is_not_element_present(*ProductPageLocators.MASSAGE_OF_PRODUCT_FROM_THE_BASKET),\
            "Success massage presented!"

    def should_be_disappeared_success_massage(self):
        assert self.is_disappeared(*ProductPageLocators.MASSAGE_OF_PRODUCT_FROM_THE_BASKET),\
            "Success massage appeared after adding product to basket"

