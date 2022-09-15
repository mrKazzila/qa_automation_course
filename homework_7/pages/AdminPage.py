from datetime import datetime

import allure
from selenium.webdriver.common.by import By

from homework_7.pages.BasePage import BasePage


class Product:
    unix_time = str(int(datetime.timestamp(datetime.now())))
    NAME: str = f'TestProduct{unix_time}'
    METE_TAG_TITLE: str = 'TestProductTag'
    MODEL: str = 'TestModel'
    PRICE: str = '1000'


class AdminPage(BasePage):
    ADD_URL: str = 'admin/'

    TITLE: str = 'Administration'
    USERNAME_FIELD: tuple = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BTN: tuple = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_BTN: tuple = (By.CSS_SELECTOR, "span[class='help-block']")

    CATALOG_BTN: tuple = (By.LINK_TEXT, 'Catalog')
    PRODUCT_BTN: tuple = (By.LINK_TEXT, "Products")
    ADD_NEW_PRODUCT_BTN: tuple = (By.CSS_SELECTOR, '[data-original-title="Add New"]')

    PRODUCT_NAME: tuple = (By.CSS_SELECTOR, "input[name='product_description[1][name]']")
    PRODUCT_METE_TAG_TITLE: tuple = (By.CSS_SELECTOR, "input[name='product_description[1][meta_title]']")
    DATA_TAB: tuple = (By.LINK_TEXT, 'Data')
    MODEL: tuple = (By.CSS_SELECTOR, "input[name='model']")
    PRICE: tuple = (By.CSS_SELECTOR, "input[name='price']")
    SAVE_BTN: tuple = (By.CSS_SELECTOR, '[data-original-title="Save"]')

    FILTER_BY_NAME_FIELD: tuple = (By.CSS_SELECTOR, "input[name='filter_name']")
    FILTER_BTN: tuple = (By.CSS_SELECTOR, "button[id='button-filter']")
    PRODUCT_FIND: tuple = (By.CSS_SELECTOR, "td[class='text-center']")
    NO_RESULT: tuple = (By.XPATH, "//td[contains(text(),'No results!')]")

    SELECT_PRODUCT: tuple = (By.CSS_SELECTOR, "input[name='selected[]']")
    PRODUCT_DELETE_BTN: tuple = (By.CSS_SELECTOR, '.btn-danger')

    @allure.step
    def open_catalog(self):
        [self._click(btn) for btn in (self.CATALOG_BTN, self.PRODUCT_BTN)]

    @allure.step
    def create_product(self):
        self._click(self.ADD_NEW_PRODUCT_BTN)

    @allure.step
    def add_new_product_info(self):
        self.logger.info(f'Add product info')
        self._wait_element(self.PRODUCT_NAME).send_keys(Product.NAME)
        self._wait_element(self.PRODUCT_METE_TAG_TITLE).send_keys(Product.METE_TAG_TITLE)
        self._click(self.DATA_TAB)
        self._wait_element(self.MODEL).send_keys(Product.MODEL)
        self._wait_element(self.PRICE).send_keys(Product.PRICE)
        self._click(self.SAVE_BTN)

    @allure.step
    def find_product(self):
        self.logger.info(f'Find product {Product.NAME}')
        self._wait_element(self.FILTER_BY_NAME_FIELD).send_keys(Product.NAME)
        self._click(self.FILTER_BTN)

    @allure.step
    def delete_product(self):
        self.logger.info(f'Delete product')
        self._click(self.SELECT_PRODUCT)
        self._click(self.PRODUCT_DELETE_BTN)
        self._accept_allert()

    @allure.step
    def check_add_product(self):
        assert len(self._wait_elements(self.PRODUCT_FIND)) > 3, "Product not added!"

    @allure.step
    def check_del_product(self):
        assert self._wait_element(self.NO_RESULT).text == "No results!", "Product not deleted!"
