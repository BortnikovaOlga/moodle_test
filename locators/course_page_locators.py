from typing import Any

from selenium.webdriver.common.by import By


class CoursePageLocators:

    SUBMIT_BUTTON = (By.ID, "id_saveanddisplay")

    SHORT_NAME_INPUT = (By.ID, "id_shortname")
    FULL_NAME_INPUT = (By.ID, "id_fullname")
    DESCRIPTION_SUMMARY_INPUT = (By.ID, "id_summary_editoreditable")
    START_YEAR = (By.ID, "id_startdate_year")
    START_MONTH = (By.ID, "id_startdate_month")
    START_DAY = (By.ID, "id_startdate_day")
    END_YEAR = (By.ID, "id_enddate_year")
    END_MONTH = (By.ID, "id_enddate_month")
    END_DAY = (By.ID, "id_enddate_day")

    COURSE_HEADER = (By.CSS_SELECTOR, "#page-header h1")
    SUBMIT_DELETE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    DELETE_HEADER = (By.XPATH, '//span[@id="maincontent"]/following-sibling::h2')

    @staticmethod
    def course_link(full_course_name: str) -> tuple[Any, str]:
        return By.XPATH, f"//a[text()='{full_course_name}']"

    @staticmethod
    def course_delete_link(full_course_name: str) -> tuple[Any, str]:
        return (
            By.XPATH,
            f"//a[text()='{full_course_name}']//following-sibling\
            ::div//a[@class='action-delete']",
        )
