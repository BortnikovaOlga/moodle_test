import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from models.auth_data import AuthData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # , chrome_options=chrome_options
    fix_app = Application(
        webdriver.Chrome(ChromeDriverManager().install()),
        base_url,
        chrome_options=chrome_options,
    )
    yield fix_app
    fix_app.quit()


@pytest.fixture
def fix_auth(app, request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_auth_page()
    app.login_page.auth(AuthData(login=user, password=password))
    assert app.login_page.is_auth(), "You are not auth"


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
