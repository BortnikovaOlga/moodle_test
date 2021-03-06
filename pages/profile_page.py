import logging
import os.path
import random
import allure
from selenium.webdriver.remote.webelement import WebElement

from log_settings import LOGGING_CONFIG
from models.person_data import PersonData
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("moodle")


class ProfilePage(BasePage):
    # == FIND ELEMENT =================================================================
    def find_basic_data_button(self) -> WebElement:
        return self.find_element(ProfilePageLocators.GENERAL_DATA_BUTTON)

    def find_login_input(self) -> WebElement:
        return self.find_element(ProfilePageLocators.LOGIN_INPUT)

    def find_firstname_input(self) -> WebElement:
        return self.find_element(ProfilePageLocators.FIRSTNAME_INPUT)

    def find_lastname_input(self) -> WebElement:
        return self.find_element(ProfilePageLocators.LASTNAME_INPUT)

    def find_email_input(self) -> WebElement:
        return self.find_element(ProfilePageLocators.EMAIL_INPUT)

    def find_email_display_select(self) -> WebElement:
        return self.find_select_element(ProfilePageLocators.MAIL_DISPLAY_SELECT)

    def find_moodle_net_profile_input(self) -> WebElement:
        return self.find_element(ProfilePageLocators.MOODLE_NET_PROFILE)

    def find_city_input(self) -> WebElement:
        return self.find_element(ProfilePageLocators.CITY_INPUT)

    def find_country_select(self) -> WebElement:
        return self.find_select_element(ProfilePageLocators.COUNTRY_SELECT)

    def find_timezone_select(self) -> WebElement:
        return self.find_select_element(ProfilePageLocators.TIME_ZONE_SELECT)

    def find_about_input(self) -> WebElement:
        return self.find_element(ProfilePageLocators.ABOUT_TEXT_AREA)

    def find_picture_add_button(self) -> WebElement:
        return self.find_element_clickable(ProfilePageLocators.PICTURE_ADD_BUTTON)

    def find_submit_button(self) -> WebElement:
        return self.find_element_clickable(ProfilePageLocators.SUBMIT_BUTTON)

    def find_file_input(self) -> WebElement:
        return self.find_element(ProfilePageLocators.FILE_INPUT)

    def find_upload_file_button(self) -> WebElement:
        return self.find_element_clickable(ProfilePageLocators.UPLOAD_FILE_BUTTON)

    # == INPUT/SELECT/SUBMIT  ======================================================

    def input_login(self, login):
        self.fill_element(self.find_login_input(), login)

    def input_firstname(self, firstname):
        self.fill_element(self.find_firstname_input(), firstname)

    def input_lastname(self, lastname):
        self.fill_element(self.find_lastname_input(), lastname)

    def input_email(self, email):
        self.fill_element(self.find_email_input(), email)

    def select_email_display(self, value):
        self.select_value(self.find_email_display_select(), value)

    def input_moodle_net_profile(self, url):
        self.fill_element(self.find_moodle_net_profile_input(), url)

    def input_city(self, city):
        self.fill_element(self.find_city_input(), city)

    def select_country(self, value):
        self.select_value(self.find_country_select(), value)

    def select_timezone(self, value):
        self.select_value(self.find_timezone_select(), value)

    def input_about(self, text):
        self.fill_element(self.find_about_input(), text)

    def submit_changes(self):
        self.click_element(self.find_submit_button())

    def input_picture(self, path_file: str):
        self.click_element(self.find_picture_add_button())
        self.fill_element(self.find_file_input(), path_file)
        self.click_element(self.find_upload_file_button())

    #  ========================================================================

    @allure.step("???????????? ???????????????????????? ????????????")
    def edit_general_personal_data(self, person=PersonData()):
        """???? ?????????????????? ???????????????????????????? ???????????????? ????????????????."""
        self.input_firstname(person.firstname)
        self.input_lastname(person.lastname)
        self.input_email(person.email)
        self.select_email_display(person.email_display)
        self.input_city(person.city)
        self.select_country(person.country)
        self.select_timezone(person.timezone)
        self.submit_changes()
        logger.info(f"Update user profile {person.__repr__()}")

    @allure.step("?????????????????? ??????????????????????")
    def load_user_picture(self):
        image_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images"
        )
        path_file = os.path.join(
            image_dir, os.path.join(random.choice(os.listdir(image_dir)))
        )
        self.input_picture(path_file)
        self.submit_changes()
        logger.info(f"Load user picture from {path_file}")

    @allure.step("?????????????????? ?????? ?????????????????? ??????????????????")
    def is_changed(self) -> bool:
        # alert_block = self.find_element(ProfilePageLocators.SUCCESS_ALERT)
        breadcrumb_menu = self.ec_find_elements(ProfilePageLocators.BREADCRUMB_MENU)
        return len(breadcrumb_menu) == 2
