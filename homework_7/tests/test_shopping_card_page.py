from homework_7.pages.CartPage import CartPage


def test_cart_page_title(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_title_contain(CartPage.TITLE)


def test_cart_page_logo(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_element(CartPage.LOGO)


def test_cart_page_search(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_element(CartPage.SEARCH)


def test_cart_page_goods(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_element(CartPage.CONTENT_FIELD)


def test_cart_page_content_field(driver, base_url):
    driver.get(f'{base_url}{CartPage.ADD_URL}')
    CartPage(driver)._wait_element(CartPage.CONTINUE_BTN, timeout=8)
