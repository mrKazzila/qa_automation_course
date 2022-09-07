from selenium.webdriver.common.by import By

from framework import wait_element, wait_title_contain


class CartPage:
    ADD_URL: str = r"index.php?route=checkout/cart"
    TITLE: str = 'Shopping Cart'
    LOGO: tuple = (By.CSS_SELECTOR, "img[title='Your Store']")
    SEARCH: tuple = (By.CSS_SELECTOR, "input[name='search']")
    CONTENT_FIELD: tuple = (By.CSS_SELECTOR, "div[id='content']")
    CONTINUE_BTN: tuple = (By.CSS_SELECTOR, "div[class='pull-right']")


def test_cart_page_title(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    wait_title_contain(driver, CartPage.TITLE)


def test_cart_page_logo(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    wait_element(driver, CartPage.LOGO)


def test_cart_page_search(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    wait_element(driver, CartPage.SEARCH)


def test_cart_page_goods(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    wait_element(driver, CartPage.CONTENT_FIELD)


def test_cart_page_content_field(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    wait_element(driver, CartPage.CONTINUE_BTN, timeout=8)
