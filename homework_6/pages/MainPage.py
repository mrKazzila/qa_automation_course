from homework_6.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from collections import namedtuple


class MainPage(BasePage):
    TITLE: str = 'Your Store'

    LOGO: tuple = (By.CSS_SELECTOR, "img[title='Your Store']")
    CART: tuple = (By.CSS_SELECTOR, "div[class='btn-group btn-block']")
    SEARCH: tuple = (By.CSS_SELECTOR, "input[name='search']")
    SLIDE_SHOW: tuple = (By.CSS_SELECTOR, "div[class='swiper-wrapper']")

    CURRENCY_BTN: tuple = (By.CSS_SELECTOR, '[class="fa fa-caret-down"]')

    EUR: tuple = (By.NAME, "EUR")
    IS_EUR_CURRENCY: tuple = (By.XPATH, '//strong[text()="€"]')
    GBP: tuple = (By.NAME, "GBP")
    IS_GBP_CURRENCY: tuple = (By.XPATH, '//strong[text()="£"]')
    USD: tuple = (By.NAME, "USD")
    IS_USD_CURRENCY: tuple = (By.XPATH, '//strong[text()="$"]')

    CURRENCY = namedtuple('Currency', 'name, check')
    CURRENCY_DATA = (
        CURRENCY(name=EUR, check=IS_EUR_CURRENCY),
        CURRENCY(name=GBP, check=IS_GBP_CURRENCY),
        CURRENCY(name=USD, check=IS_USD_CURRENCY),
    )

    def switch_currency(self):
        for currency in self.CURRENCY_DATA:
            self._click(self.CURRENCY_BTN)
            self._click(currency.name)
            self._wait_element(currency.check)
