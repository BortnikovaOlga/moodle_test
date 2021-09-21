from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "loginbtn")

    LOGIN_ERROR = (By.ID, "loginerrormessage")

    FORM = (By.ID, "page-wrapper")

    USER_BUTTON = (By.ID, "action-menu-toggle-1")
    USER_MENU = (By.CLASS_NAME, "usermenu")

    EXIT = (By.ID, "actionmenuaction-6")
    EXIT_CONFIRM = (By.XPATH, "//button[text()='Выход']")
