import allure

from homework_7.pages.CartPage import CartPage


@allure.step('Проверяю тайтл страницы')
def test_cart_page_title(driver, base_url):
    CartPage(driver)._open_url(url=f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_title_contain(CartPage.TITLE)


@allure.step('Проверяю наличие лого на странице корзины')
def test_cart_page_logo(driver, base_url):
    CartPage(driver)._open_url(url=f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_element(CartPage.LOGO)


@allure.step('Проверяю наличие поиска на странице корзины')
def test_cart_page_search(driver, base_url):
    CartPage(driver)._open_url(url=f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_element(CartPage.SEARCH)


@allure.step('Проверяю товар в корзине')
def test_cart_page_goods(driver, base_url):
    CartPage(driver)._open_url(url=f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_element(CartPage.CONTENT_FIELD)


@allure.step('Проверяю наличие кнопик продолжить')
def test_cart_page_content_field(driver, base_url):
    CartPage(driver)._open_url(url=f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_element(CartPage.CONTINUE_BTN, timeout=8)
