from typing import Any

from selenium.webdriver.common.by import By


class CoursePageLocators:
    SUBMIT_BUTTON = (By.ID, "id_saveanddisplay")
    SHORT_NAME_INPUT = (By.ID, "id_shortname")
    FULL_NAME_INPUT = (By.ID, "id_fullname")
    COURSE_HEADER = (By.CSS_SELECTOR, "#page-header h1")

    @staticmethod
    def course_link(full_course_name: str) -> tuple[Any, str]:
        return By.XPATH, f"//a[text()='{full_course_name}']"
