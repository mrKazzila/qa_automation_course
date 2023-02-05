import allure
from pages.MainPage import MainPage


@allure.step('Проверка названия страницы')
def test_main_page_title(driver, base_url):
    MainPage(driver)._open_url(url=base_url)
    MainPage(driver)._wait_title_contain(MainPage.TITLE)


@allure.step('Проверка наличия логотипа')
def test_main_page_logo(driver, base_url):
    MainPage(driver)._open_url(url=base_url)
    MainPage(driver)._wait_element(MainPage.LOGO)


@allure.step('Проверка наличия корзины')
def test_main_page_cart(driver, base_url):
    MainPage(driver)._open_url(url=base_url)
    MainPage(driver)._wait_element(MainPage.CART)


@allure.step('Проверка наличия строки поиска')
def test_main_page_search(driver, base_url):
    MainPage(driver)._open_url(url=base_url)
    MainPage(driver)._wait_element(MainPage.SEARCH)


@allure.step('Проверка наличия товара на главной странице')
def test_main_page_goods(driver, base_url):
    MainPage(driver)._open_url(url=base_url)
    MainPage(driver)._wait_element(MainPage.SLIDE_SHOW)


@allure.step('Тест на смену валюты на главной странице')
def test_switch_currency(driver, base_url):
    MainPage(driver)._open_url(url=base_url)
    MainPage(driver).switch_currency()
