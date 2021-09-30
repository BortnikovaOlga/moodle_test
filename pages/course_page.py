import datetime

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from models.course_data import CourseData
from pages.base_page import BasePage
from locators.course_page_locators import CoursePageLocators
from common.constants import CourseConstants


class CoursePage(BasePage):
    def input_full_name(self, full_name: str):
        self.fill_element(self.find_full_name_input(), full_name)

    def input_short_name(self, short_name: str):
        self.fill_element(self.find_short_name_input(), short_name)

    def input_description(self, description: str):
        self.fill_element(self.find_description_input(), description)

    def input_date_start(self, date_start: datetime.date):
        self.select_value(self.find_date_start_day_select(), str(date_start.day))
        self.select_value(self.find_date_start_month_select(), str(date_start.month))
        self.select_value(self.find_date_start_year_select(), date_start.strftime("%Y"))

    def input_date_end(self, date_end: datetime.date):
        self.select_value(self.find_date_end_day_select(), str(date_end.day))
        self.select_value(self.find_date_end_month_select(), str(date_end.month))
        self.select_value(self.find_date_end_year_select(), date_end.strftime("%Y"))

    def find_full_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.FULL_NAME_INPUT)

    def find_short_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.SHORT_NAME_INPUT)

    def find_description_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.DESCRIPTION_SUMMARY_INPUT)

    def find_submit_button(self) -> WebElement:
        return self.find_element_clickable(CoursePageLocators.SUBMIT_BUTTON)

    def find_date_start_day_select(self) -> Select:
        return self.find_select_element(CoursePageLocators.START_DAY)

    def find_date_start_month_select(self) -> Select:
        return self.find_select_element(CoursePageLocators.START_MONTH)

    def find_date_start_year_select(self) -> Select:
        return self.find_select_element(CoursePageLocators.START_YEAR)

    def find_date_end_day_select(self) -> Select:
        return self.find_select_element(CoursePageLocators.END_DAY)

    def find_date_end_month_select(self) -> Select:
        return self.find_select_element(CoursePageLocators.END_MONTH)

    def find_date_end_year_select(self) -> Select:
        return self.find_select_element(CoursePageLocators.END_YEAR)

    def find_delete_course_button(self, full_name) -> WebElement:
        return self.find_element(CoursePageLocators.course_delete_link(full_name))

    def find_confirm_delete_button(self) -> WebElement:
        return self.find_element(CoursePageLocators.SUBMIT_DELETE_BUTTON)

    def submit_changes(self):
        self.click_element(self.find_submit_button())

    @allure.step("заполнить данные о курсе")
    def edit_general_course_data(self, course=CourseData.random()):
        self.input_full_name(course.full_name)
        self.input_short_name(course.short_name)
        self.input_description(course.summary)
        self.input_date_start(course.date_start)
        self.input_date_end(course.date_end)
        self.submit_changes()
        return course.full_name

    def is_find_add_course_header(self, full_name: str) -> bool:
        course_header = self.find_elements(CoursePageLocators.COURSE_HEADER)
        return not (len(course_header) == 0 or course_header[0].text != full_name)

    def is_find_delete_course_header(self, short_name: str) -> bool:
        delete_headers = self.ec_find_elements(CoursePageLocators.DELETE_HEADER)
        return not (
            len(delete_headers) == 0
            or delete_headers[0].text != CourseConstants.DELETE_HEADER + short_name
        )

    @allure.step("проверить сообщение о добавлении нового курса")
    def is_added_course(self, full_name: str) -> bool:
        return self.is_find_add_course_header(full_name)

    @allure.step("проверить сообщение что курс удален")
    def is_deleted_course(self, short_name: str) -> bool:
        return self.is_find_delete_course_header(short_name)

    @allure.step("удалить курс по названию")
    def delete_course(self, full_name: str):
        self.click_element(self.find_delete_course_button(full_name))
        self.click_element(self.find_confirm_delete_button())
