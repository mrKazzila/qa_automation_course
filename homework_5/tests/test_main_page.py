from framework import wait_element, wait_title_contain
from selenium.webdriver.common.by import By


class MainPage:
    TITLE: str = 'Your Store'
    LOGO: tuple = (By.CSS_SELECTOR, 'img[title="Your Store"]')
    CART: tuple = (By.CSS_SELECTOR, 'div[class="btn-group btn-block"]')
    SEARCH: tuple = (By.CSS_SELECTOR, 'input[name="search"]')
    SLIDE_SHOW: tuple = (By.CSS_SELECTOR, 'div[class="swiper-wrapper"]')


def test_main_page_title(driver, base_url):
    driver.get(base_url)
    wait_title_contain(driver, MainPage.TITLE)


def test_main_page_logo(driver, base_url):
    driver.get(base_url)
    wait_element(driver, MainPage.LOGO)


def test_main_page_cart(driver, base_url):
    driver.get(base_url)
    wait_element(driver, MainPage.CART)


def test_main_page_search(driver, base_url):
    driver.get(base_url)
    wait_element(driver, MainPage.SEARCH)


def test_main_page_goods(driver, base_url):
    driver.get(base_url)
    wait_element(driver, MainPage.SLIDE_SHOW)
