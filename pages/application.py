from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from pages.profile_page import ProfilePage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login_page = LoginPage(self)
        self.nav_bar = NavBar(self)
        self.profile_page = ProfilePage(self)

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()
