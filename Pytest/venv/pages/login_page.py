from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login' in self.url, 'No \'/login\' in URL!'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is absent or check locator'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is absent or check locator'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REGISTRATION).\
            send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FOR_REGISTRATION).\
            send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FOR_REGISTRATION).\
            send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()
