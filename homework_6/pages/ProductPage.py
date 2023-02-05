from selenium.webdriver.common.by import By

from homework_6.pages.BasePage import BasePage


class ProductPage(BasePage):
    ADD_URL: str = r'/desktops'
    TITLE: str = 'Desktops'

    LOGO: tuple = (By.CSS_SELECTOR, 'img[title="Your Store"]')
    GOODS_GROUPS: tuple = (By.CSS_SELECTOR, 'div[class="list-group"]')
    DESCRIPTION_FIELD: tuple = (By.CSS_SELECTOR, 'div[class="col-sm-10"]')
    IMAGE_FIELD: tuple = (By.CSS_SELECTOR, 'div[class="col-sm-2"]')
