import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--drivers",
        default=os.path.expanduser("drivers"),
        help="This is default path with drivers",
        action="store"
    )
    parser.addoption(
        "--browser",
        default="chrome",
        help="This is default browser",
        action="store"
    )
    parser.addoption(
        "--url",
        default="http://192.168.0.179:8081/",
        help='This is default url',
        action="store"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def driver(request):
    driver = request.config.getoption("--drivers")
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=f'{driver}/chromedriver')
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=f'{driver}/geckodriver')
    elif browser_name == "opera":
        # fix bug with dict https://github.com/operasoftware/operachromiumdriver/issues/96#issuecomment-985291083
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', True)
        browser = webdriver.Opera(executable_path=f'{driver}/operadriver', options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported!")

    browser.maximize_window()
    request.addfinalizer(browser.quit)

    return browser
