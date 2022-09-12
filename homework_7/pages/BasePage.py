import functools
import logging
import os
import traceback as tb
from typing import Any

import allure
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

    @allure.step
    def _open_url(self, url: str):
        self.logger.info(f'Open url: {url}')
        self.driver.get(url)

    @allure.step
    def _wait_title_contain(self, text: str, timeout: float = 3) -> Any:
        try:
            self.logger.info(f'Wait page title: {text}')
            WebDriverWait(self.driver, timeout).until(
                EC.title_contains(text)
            )
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'FAILED Not found title with text {text}'
            )
            raise AssertionError(f'Not wait {text} in page title')

    @allure.step
    def _wait_element(self, locator: tuple, timeout: float = 10) -> webelement:
        try:
            self.logger.info(f'Wait element: {locator}')
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'FAILED Not found element with locator={locator}'
            )
            raise AssertionError(f'Not wait {locator} in page')

    @allure.step
    def _wait_elements(self, locator: tuple, timeout: float = 10) -> webelement:
        try:
            self.logger.info(f'Wait elements: {locator}')
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'FAILED Not found {locator}'
            )
            raise AssertionError(f'Not wait {locator} in page')

    @allure.step
    def _element(self, locator: tuple) -> webelement:
        return self._wait_element(locator=locator)

    @allure.step
    def _click(self, locator: tuple) -> Any:
        element = self._element(locator)
        self.logger.info(f'Click on: {element}')
        ActionChains(self.driver).pause(0.2).move_to_element(element).click().perform()

    @allure.step
    def _accept_allert(self) -> Any:
        self.logger.info('Accept allert')
        self.driver.switch_to.alert.accept()

    @staticmethod
    def check_test(funk):
        @functools.wraps(funk)
        def wrapper(*args, **kwargs):
            try:
                funk(*args, **kwargs)
            except Exception as error:
                allure.attach(
                    body=BasePage(kwargs.get('driver')).driver.get_screenshot_as_png(),
                    name=f'{funk.__name__}_error'
                )
                BasePage(kwargs.get('driver')).logger.error(
                    f'{tb.format_exception(type(error), error, error.__traceback__)}'
                )
                raise error

        return wrapper
