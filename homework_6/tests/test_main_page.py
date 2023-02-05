from homework_6.pages.MainPage import MainPage


def test_main_page_title(driver, base_url):
    driver.get(base_url)
    MainPage(driver)._wait_title_contain(MainPage.TITLE)


def test_main_page_logo(driver, base_url):
    driver.get(base_url)
    MainPage(driver)._wait_element(MainPage.LOGO)


def test_main_page_cart(driver, base_url):
    driver.get(base_url)
    MainPage(driver)._wait_element(MainPage.CART)


def test_main_page_search(driver, base_url):
    driver.get(base_url)
    MainPage(driver)._wait_element(MainPage.SEARCH)


def test_main_page_goods(driver, base_url):
    driver.get(base_url)
    MainPage(driver)._wait_element(MainPage.SLIDE_SHOW)


def test_switch_currency(driver, base_url):
    driver.get(base_url)
    MainPage(driver).switch_currency()
