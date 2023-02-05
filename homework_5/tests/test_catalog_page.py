from framework import wait_element, wait_title_contain
from selenium.webdriver.common.by import By


class CatalogPage:
    ADD_URL: str = r"/desktops"
    TITLE: str = 'Desktops'
    LOGO: tuple = (By.CSS_SELECTOR, "img[title='Your Store']")
    GOODS_GROUPS: tuple = (By.CSS_SELECTOR, "div[class='list-group']")
    DESCRIPTION_FIELD: tuple = (By.CSS_SELECTOR, "div[class='col-sm-10']")
    IMAGE_FIELD: tuple = (By.CSS_SELECTOR, "div[class='col-sm-2']")


def test_catalog_page_title(driver, base_url):
    driver.get(f"{base_url}{CatalogPage.ADD_URL}")
    wait_title_contain(driver, CatalogPage.TITLE)


def test_catalog_page_shop_logo(driver, base_url):
    driver.get(f"{base_url}{CatalogPage.ADD_URL}")
    wait_element(driver, CatalogPage.LOGO)


def test_catalog_page_goods_groups(driver, base_url):
    driver.get(f"{base_url}{CatalogPage.ADD_URL}")
    wait_element(driver, CatalogPage.GOODS_GROUPS)


def test_catalog_page_check_description_field(driver, base_url):
    driver.get(f"{base_url}{CatalogPage.ADD_URL}")
    wait_element(driver, CatalogPage.DESCRIPTION_FIELD)


def test_catalog_page_image_field(driver, base_url):
    driver.get(f"{base_url}{CatalogPage.ADD_URL}")
    wait_element(driver, CatalogPage.IMAGE_FIELD)
