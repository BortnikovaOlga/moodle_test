from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_element_clickable(self, locator, wait_time=15):
        return WebDriverWait(self.app.driver, wait_time).until(
            EC.element_to_be_clickable(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator):
        return self.app.driver.find_elements(*locator)

    def ec_find_elements(self, locator, wait_time=10):
        """Ищет эелементы с явным ожиданием."""
        return WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def find_select_element(self, locator):
        return Select(self.find_element(locator))

    @staticmethod
    def select_value(select_element, value):
        select_element.select_by_value(value)

    @staticmethod
    def fill_element(element, text):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    @staticmethod
    def click_element(element):
        element.click()
