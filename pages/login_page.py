import logging.config
import allure
from selenium.webdriver.remote.webelement import WebElement

from models.auth_data import AuthData
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from log_settings import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    @allure.step("проверить что авторизованы")
    def is_auth(self):
        self.find_element(LoginPageLocators.FORM)
        return len(self.find_elements(LoginPageLocators.USER_BUTTON)) > 0

    @allure.step("авторизация")
    def auth(self, data: AuthData):
        logger.info(f"Login with username={data.login} password={data.password}")
        if self.is_exit_confirm_button():
            self.click_element(self.find_exit_confirm())
        else:
            self.sign_out()
        self.fill_element(self.find_login_input(), data.login)
        self.fill_element(self.find_password_input(), data.password)
        self.click_element(self.find_submit_button())

    def find_login_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN)

    def find_password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD)

    def find_submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.SUBMIT)

    def find_user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def find_exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT)

    def find_exit_confirm(self):
        return self.find_element(LoginPageLocators.EXIT_CONFIRM)

    def is_exit_confirm_button(self):
        return len(self.find_elements(LoginPageLocators.EXIT_CONFIRM))

    @allure.step("проверить сообщение ошибки авторизации")
    def auth_error_text(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text

    def sign_out(self):
        if self.is_auth():
            self.click_element(self.find_user_menu())
            self.click_element(self.find_exit())
