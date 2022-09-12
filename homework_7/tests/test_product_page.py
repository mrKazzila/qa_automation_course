from homework_7.pages.ProductPage import ProductPage


def test_product_page_title(driver, base_url):
    ProductPage(driver)._open_url(url=f"{base_url}{ProductPage.ADD_URL}")
    ProductPage(driver)._wait_title_contain(ProductPage.TITLE)


def test_product_page_shop_logo(driver, base_url):
    ProductPage(driver)._open_url(url=f"{base_url}{ProductPage.ADD_URL}")
    ProductPage(driver)._wait_element(ProductPage.LOGO)


def test_product_page_goods_groups(driver, base_url):
    ProductPage(driver)._open_url(url=f"{base_url}{ProductPage.ADD_URL}")
    ProductPage(driver)._wait_element(ProductPage.GOODS_GROUPS)


def test_product_page_check_description_field(driver, base_url):
    ProductPage(driver)._open_url(url=f"{base_url}{ProductPage.ADD_URL}")
    ProductPage(driver)._wait_element(ProductPage.DESCRIPTION_FIELD)


def test_product_page_image_field(driver, base_url):
    ProductPage(driver)._open_url(url=f"{base_url}{ProductPage.ADD_URL}")
    ProductPage(driver)._wait_element(ProductPage.IMAGE_FIELD)
