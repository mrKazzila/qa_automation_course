from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def wait_title_contain(driver: webdriver, text: str, timeout: float = 3):
    try:
        WebDriverWait(driver, timeout).until(
            ec.title_contains(text),
        )
    except TimeoutException:
        raise AssertionError(f'Not wait {text} in page title')


def wait_element(driver: webdriver, locator: tuple, timeout: float = 10):
    try:
        WebDriverWait(driver, timeout).until(
            ec.visibility_of_element_located(locator),
        )
    except TimeoutException:
        raise AssertionError(f'Not wait {locator} in page')
