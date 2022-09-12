import logging
import os
from typing import NoReturn

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote import webdriver, webelement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.__config_logger()

    def __config_logger(self, to_file=True):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    def _open_url(self, url: str):
        self.logger.info(f'Open url: {url}')
        self.driver.get(url)

    def _wait_title_contain(self, text: str, timeout: float = 3) -> NoReturn:
        try:
            self.logger.info(f'Wait page title: {text}')
            WebDriverWait(self.driver, timeout).until(
                EC.title_contains(text)
            )
        except TimeoutException:
            raise AssertionError(f'Not wait {text} in page title')

    def _wait_element(self, locator: tuple, timeout: float = 10) -> webelement:
        try:
            self.logger.info(f'Wait element: {locator}')
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f'Not wait {locator} in page')

    def _wait_elements(self, locator: tuple, timeout: float = 10) -> webelement:
        try:
            self.logger.info(f'Wait elements: {locator}')
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f'Not wait {locator} in page')

    def _element(self, locator: tuple) -> webelement:
        return self._wait_element(locator=locator)

    def _click(self, locator: tuple) -> NoReturn:
        element = self._element(locator)
        self.logger.info(f'Click on: {element}')
        ActionChains(self.driver).pause(0.2).move_to_element(element).click().perform()

    def _accept_allert(self) -> NoReturn:
        self.logger.info('Accept allert')
        self.driver.switch_to.alert.accept()

