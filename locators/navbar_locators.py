from selenium.webdriver.common.by import By


class NavBarLocators:
    USER_MENU = (By.ID, "action-menu-toggle-1")
    USER_MENU_PROFILE = (
        By.ID,
        "actionmenuaction-2",
    )
    USER_MENU_PREFERENCES = (
        By.ID,
        "actionmenuaction-5",
    )
    USER_MENU_EXIT = (By.ID, "actionmenuaction-6")

    LEFT_MENU_BUTTON = (By.CSS_SELECTOR, "button.float-sm-left")
    LEFT_MENU_ADMIN_ITEM = (
        By.CSS_SELECTOR,
        'a.list-group-item[href=\
        "https://qacoursemoodle.innopolis.university/admin/search.php"]',
    )
    NAV_TABS_COURSES = (By.CSS_SELECTOR, 'ul.nav-tabs a[href="#linkcourses"]')
    ADD_NEW_COURSE_LINK = (
        By.CSS_SELECTOR,
        'a[href=\
        "https://qacoursemoodle.innopolis.university/course/edit.php?category=0"]',
    )
    MENAGE_COURSES_LINK = (
        By.CSS_SELECTOR,
        'a[href=\
        "https://qacoursemoodle.innopolis.university/course/management.php"]',
    )

    MAIN_CONTENT_TITLE = (By.XPATH, '//span[@id="maincontent"]/following-sibling::h2')
