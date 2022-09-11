from homework_7.pages.AdminPage import AdminPage
from homework_7.pages.elements.LoginForms import AdminLoginForm


def test_admin_page_title(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_title_contain(AdminPage.TITLE)


def test_admin_page_username_field(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_element(AdminPage.USERNAME_FIELD)


def test_admin_page_password_field(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_element(AdminPage.PASSWORD_FIELD)


def test_admin_page_login_btn(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_element(AdminPage.LOGIN_BTN)


def test_admin_page_forgotten_btn(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_element(AdminPage.LOGIN_BTN)


def test_admin_add_new_good(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    AdminLoginForm(driver).admin_login()
    AdminPage(driver).open_catalog()
    AdminPage(driver).create_product()
    AdminPage(driver).add_new_product_info()
    AdminPage(driver).find_product()
    AdminPage(driver).check_add_product()


def test_admin_del_new_good(driver, base_url):
    driver.get(f'{base_url}{AdminPage.ADD_URL}')
    AdminLoginForm(driver).admin_login()
    AdminPage(driver).open_catalog()
    AdminPage(driver).find_product()
    AdminPage(driver).delete_product()
    AdminPage(driver).check_del_product()
