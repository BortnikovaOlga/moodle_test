from selenium.webdriver.remote.webelement import WebElement

from models.course_data import CourseData
from pages.base_page import BasePage
from locators.course_page_locators import CoursePageLocators


class CoursePage(BasePage):
    def input_full_name(self, full_name):
        self.fill_element(self.find_full_name_input(), full_name)

    def input_short_name(self, short_name):
        self.fill_element(self.find_short_name_input(), short_name)

    def find_full_name_input(self):
        return self.find_element(CoursePageLocators.FULL_NAME_INPUT)

    def find_short_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.SHORT_NAME_INPUT)

    def find_submit_button(self) -> WebElement:
        return self.find_element_clickable(CoursePageLocators.SUBMIT_BUTTON)

    def submit_changes(self):
        self.click_element(self.find_submit_button())

    def edit_general_course_data(self, course=CourseData.random()):
        self.input_full_name(course.full_name)
        self.input_short_name(course.short_name)
        self.submit_changes()

    def is_add_course(self):
        """Заглушка."""
        return True
