from typing import NoReturn

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote import webdriver, webelement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def _wait_title_contain(self, text: str, timeout: float = 3) -> NoReturn:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.title_contains(text)
            )
        except TimeoutException:
            raise AssertionError(f'Not wait {text} in page title')

    def _wait_element(self, locator: tuple, timeout: float = 10) -> webelement:
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f'Not wait {locator} in page')

    def _wait_elements(self, locator: tuple, timeout: float = 10) -> webelement:
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f'Not wait {locator} in page')

    def _element(self, locator: tuple) -> webelement:
        return self._wait_element(locator=locator)

    def _click(self, locator: tuple) -> NoReturn:
        element = self._element(locator)
        ActionChains(self.driver).pause(0.2).move_to_element(element).click().perform()

    def _accept_allert(self) -> NoReturn:
        self.driver.switch_to.alert.accept()

