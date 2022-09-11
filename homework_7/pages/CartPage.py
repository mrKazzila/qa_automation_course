from selenium.webdriver.common.by import By

from homework_7.pages.BasePage import BasePage


class CartPage(BasePage):
    ADD_URL: str = r"index.php?route=checkout/cart"
    TITLE: str = 'Shopping Cart'

    LOGO: tuple = (By.CSS_SELECTOR, "img[title='Your Store']")
    SEARCH: tuple = (By.CSS_SELECTOR, "input[name='search']")
    CONTENT_FIELD: tuple = (By.CSS_SELECTOR, "div[id='content']")
    CONTINUE_BTN: tuple = (By.CSS_SELECTOR, "div[class='pull-right']")
