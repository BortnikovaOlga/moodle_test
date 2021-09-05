from selenium.webdriver.remote.webelement import WebElement

from locators.navbar_locators import NavBarLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class NavBar(BasePage):
    def find_user_menu(self) -> WebElement:
        return self.find_element(NavBarLocators.USER_MENU)

    def find_user_menu_preferences(self) -> WebElement:
        return self.find_element(NavBarLocators.USER_MENU_PREFERENCES)

    def find_edit_profile_link(self) -> WebElement:
        return self.find_element(ProfilePageLocators.EDIT_PROFILE_LINK)

    def user_menu_profile(self) -> WebElement:
        return self.find_element(NavBarLocators.USER_MENU_PROFILE)

    def user_menu_exit(self) -> WebElement:
        return self.find_element(NavBarLocators.USER_MENU_EXIT)

    def exit(self):
        self.click_element(self.find_user_menu())
        self.click_element(self.user_menu_exit())

    def open_profile_page(self):
        self.click_element(self.find_user_menu())
        self.click_element(self.find_user_menu_preferences())
        self.click_element(self.find_edit_profile_link())
