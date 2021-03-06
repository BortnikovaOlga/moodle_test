import allure
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

    def find_user_menu_exit(self) -> WebElement:
        return self.find_element(NavBarLocators.USER_MENU_EXIT)

    def exit(self):
        self.click_element(self.find_user_menu())
        self.click_element(self.find_user_menu_exit())

    @allure.step("перейти на страницу персональных данных")
    def open_profile_page(self):
        self.click_element(self.find_user_menu())
        self.click_element(self.find_user_menu_preferences())
        self.click_element(self.find_edit_profile_link())

    def find_left_menu_button(self) -> WebElement:
        return self.find_element(NavBarLocators.LEFT_MENU_BUTTON)

    def find_admin_item(self) -> WebElement:
        return self.find_element_clickable(NavBarLocators.LEFT_MENU_ADMIN_ITEM)

    def find_nav_tab_courses(self) -> WebElement:
        return self.find_element(NavBarLocators.NAV_TABS_COURSES)

    def find_add_new_course(self):
        return self.find_element_clickable(NavBarLocators.ADD_NEW_COURSE_LINK)

    def find_menage_courses(self):
        return self.find_element_clickable(NavBarLocators.MENAGE_COURSES_LINK)

    def find_main_content_title(self) -> WebElement:
        return self.find_element(NavBarLocators.MAIN_CONTENT_TITLE)

    def expand_left_menu(self):
        left_menu_button = self.find_left_menu_button()
        if not left_menu_button.get_attribute("aria-expanded"):
            self.click_element(left_menu_button)

    @allure.step("открыть страницу добавления нового курса")
    def open_add_course_page(self) -> str:
        self.expand_left_menu()
        self.click_element(self.find_admin_item())
        self.click_element(self.find_nav_tab_courses())
        self.click_element(self.find_add_new_course())
        return self.find_main_content_title().text

    @allure.step("открыть страницу управления курсами")
    def open_menage_course_page(self):
        self.expand_left_menu()
        self.click_element(self.find_admin_item())
        self.click_element(self.find_nav_tab_courses())
        self.click_element(self.find_menage_courses())
