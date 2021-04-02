from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_FOR_NEGATIVE = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, "span.btn-group a")

class BasketPageLocators():
    PRODUCT_IN_THE_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner p")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")
    MASSAGE_OF_PRODUCT_FROM_THE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)> div>strong")
    NAME_OF_THE_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_THE_PRODUCT = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRICE_OF_THE_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
