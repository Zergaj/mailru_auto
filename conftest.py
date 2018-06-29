from _pytest.fixtures import fixture
from model.browser import Browser
from model.application import Application

import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type")
    parser.addoption("--base_url", action="store", default="https://mail.ru", help="base URL")
    parser.addoption("--path", action="store", default="chromedriver", help="path to browser")


# MAIN FIXTURES
@fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@fixture(scope="session")
def base(browser_type, base_url):
    driver = Browser(browser_type).create()
    driver.maximize_window()
    yield Application(driver, base_url)
    driver.close()
