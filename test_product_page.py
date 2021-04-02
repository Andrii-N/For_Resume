import pytest
import time
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        email = str(time.time()) + "@email.com"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_be_product_price_info()
        page.add_to_basket()
        page.should_be_massages_regarding_product_in_the_basket()
        page.should_be_same_product_name_in_massage_and_selected_product_name()
        page.should_be_same_price_of_the_product_and_basket()

    def test_user_cannot_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_no_success_massage()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_add_to_basket()

@pytest.mark.xfail
def test_guest_cannot_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_no_success_massage()


def test_guest_cannot_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_no_success_massage()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_success_massage()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cannot_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_empty_basket_massage()
