from selenium.webdriver.common.by import By


class CoursePageLocators:
    SUBMIT_BUTTON = (By.ID, "id_saveanddisplay")
    SHORT_NAME_INPUT = (By.ID, "id_shortname")
    FULL_NAME_INPUT = (By.ID, "id_fullname")
