from selenium.webdriver.remote.webelement import WebElement

from models.course_data import CourseData
from pages.base_page import BasePage
from locators.course_page_locators import CoursePageLocators
from common.constants import CourseConstants


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
        return course.full_name

    def is_added_course(self, full_name):
        return self.is_find_add_course_header(full_name)

    def is_deleted_course(self, short_name):
        return self.is_find_delete_course_header(short_name)

    def is_find_add_course_header(self, full_name):
        course_header = self.find_elements(CoursePageLocators.COURSE_HEADER)
        return not (len(course_header) == 0 or course_header[0].text != full_name)

    def delete_course(self, full_name):
        self.click_element(self.find_delete_course_button(full_name))
        self.click_element(self.find_confirm_delete_button())

    def find_delete_course_button(self, full_name):
        return self.find_element(CoursePageLocators.course_delete_link(full_name))

    def find_confirm_delete_button(self):
        return self.find_element(CoursePageLocators.SUBMIT_DELETE_BUTTON)

    def is_find_delete_course_header(self, short_name):
        delete_headers = self.ec_find_elements(CoursePageLocators.DELETE_HEADER)
        return not (
            len(delete_headers) == 0
            or delete_headers[0].text != CourseConstants.DELETE_HEADER + short_name
        )
