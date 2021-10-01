import allure

from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from pages.profile_page import ProfilePage
from pages.course_page import CoursePage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login_page = LoginPage(self)
        self.nav_bar = NavBar(self)
        self.profile_page = ProfilePage(self)
        self.course_page = CoursePage(self)

    @allure.step("открыть страницу авторизации")
    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")
        self.driver.maximize_window()

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()
