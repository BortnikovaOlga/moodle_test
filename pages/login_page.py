from selenium.webdriver.remote.webelement import WebElement

from models.auth_data import AuthData
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def is_auth(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(LoginPageLocators.USER_BUTTON)
        return len(element) > 0

    def auth(self, data: AuthData):
        if self.is_exit_confirm_button():
            self.click_element(self.exit_confirm())
        elif self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        self.fill_element(self.login_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def login_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.SUBMIT)

    def user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT)

    def exit_confirm(self):
        return self.find_element(LoginPageLocators.EXIT_CONFIRM)

    def is_exit_confirm_button(self):
        return len(self.find_elements(LoginPageLocators.EXIT_CONFIRM))

    def auth_error_text(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text
