import allure

from homework_7.pages.AdminPage import AdminPage
from homework_7.pages.elements.LoginForms import AdminLoginForm


@allure.step('Проверяю тайтл страницы')
def test_admin_page_title(driver, base_url):
    AdminPage(driver)._open_url(url=f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_title_contain(AdminPage.TITLE)


@allure.step('Проверка наличия поля для ввода username')
def test_admin_page_username_field(driver, base_url):
    AdminPage(driver)._open_url(url=f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_element(AdminPage.USERNAME_FIELD)


@allure.step('Проверка наличия поля для ввода password')
def test_admin_page_password_field(driver, base_url):
    AdminPage(driver)._open_url(url=f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_element(AdminPage.PASSWORD_FIELD)


@allure.step('Проверка наличия кнопки логина')
def test_admin_page_login_btn(driver, base_url):
    AdminPage(driver)._open_url(url=f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_element(AdminPage.LOGIN_BTN)


@allure.step('Проверка наличия кнопки восстановления пароля')
def test_admin_page_forgotten_btn(driver, base_url):
    AdminPage(driver)._open_url(url=f'{base_url}{AdminPage.ADD_URL}')
    AdminPage(driver)._wait_element(AdminPage.LOGIN_BTN)


@allure.step('Тест на добалвение нового товара')
def test_admin_add_new_good(driver, base_url):
    AdminPage(driver)._open_url(url=f'{base_url}{AdminPage.ADD_URL}')
    AdminLoginForm(driver).admin_login()
    AdminPage(driver).open_catalog()
    AdminPage(driver).create_product()
    AdminPage(driver).add_new_product_info()
    AdminPage(driver).find_product()
    AdminPage(driver).check_add_product()


@allure.step('Тест на удаления товара')
def test_admin_del_new_good(driver, base_url):
    AdminPage(driver)._open_url(url=f'{base_url}{AdminPage.ADD_URL}')
    AdminLoginForm(driver).admin_login()
    AdminPage(driver).open_catalog()
    AdminPage(driver).find_product()
    AdminPage(driver).delete_product()
    AdminPage(driver).check_del_product()
