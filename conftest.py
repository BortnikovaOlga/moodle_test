import logging.config
import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from models.auth_data import AuthData
from pages.application import Application

from log_settings import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("moodle")


@allure.step("открыть главную страницу")
@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    headless_mode = request.config.getoption("--headless").lower()
    logger.info(f"Start moodle {base_url} with headless={headless_mode} mode")
    if headless_mode == "true":
        chrome_options = Options()
        chrome_options.headless = True
        fix_app = Application(
            webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
            base_url,
        )
    elif headless_mode == "false":
        fix_app = Application(
            webdriver.Chrome(ChromeDriverManager().install()),
            base_url,
        )
    else:
        raise pytest.UsageError("--headless should be true or false")
    yield fix_app
    fix_app.quit()


@pytest.fixture
def fix_auth(app, request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_auth_page()
    app.login_page.auth(AuthData(login=user, password=password))
    assert app.login_page.is_auth(), "You are not auth"
    yield
    app.login_page.sign_out()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="bortolga",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="o08072006B+",
        help="enter password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    ),


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "app" in item.fixturenames:
                web_driver = item.funcargs["app"]
            else:
                logger.error("Fail to take screen-shot")
                return
            logger.info("Screen-shot done")
            allure.attach(
                web_driver.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            logger.error("Fail to take screen-shot: {}".format(e))
