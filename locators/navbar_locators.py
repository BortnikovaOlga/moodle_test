from selenium.webdriver.common.by import By


class NavBarLocators:
    # USER_MENU = (By.CLASS_NAME, "usermenu")
    USER_MENU = (By.ID, "action-menu-toggle-1")  # (By.CLASS_NAME, "userbutton")
    USER_MENU_PROFILE = (
        By.ID,
        "actionmenuaction-2",
    )  # (By.PARTIAL_LINK_TEXT, "profile.php")
    USER_MENU_PREFERENCES = (
        By.ID,
        "actionmenuaction-5",
    )  # (By.PARTIAL_LINK_TEXT, "preferences.php")
    USER_MENU_EXIT = (By.ID, "actionmenuaction-6")
