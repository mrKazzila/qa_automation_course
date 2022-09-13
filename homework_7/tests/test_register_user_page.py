import allure
import pytest

from homework_7.pages.UserPage import UserPage


@allure.step('Проверяю тайтл страницы')
def test_register_page_title(driver, base_url):
    UserPage(driver)._open_url(url=f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_title_contain(UserPage.TITLE)


@allure.step('Проверяю наичие поля для ввода имени')
def test_register_page_name_field(driver, base_url):
    UserPage(driver)._open_url(url=f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_element(UserPage.FIRST_NAME_FIELD)


@allure.step('Проверяю наличие радиобатона подписки')
def test_register_page_subscribe_btn(driver, base_url):
    UserPage(driver)._open_url(url=f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_element(UserPage.SUBSCRIBE_BTN)


@allure.step('Проверяю наличие кнопки продолжить')
def test_register_page_continue_btn(driver, base_url):
    UserPage(driver)._open_url(url=f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_element(UserPage.CONTINUE_BUTTON)


@allure.step('Проверяю наличие чекбокса политики безопасности')
def test_register_page_privacy_checkbox_btn(driver, base_url):
    UserPage(driver)._open_url(url=f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_element(UserPage.PRIVACY_CHECKBOX_BTN)


@allure.step('Тест на регистрацию нового пользователя')
def test_registration_new_user(driver, base_url):
    UserPage(driver)._open_url(url=f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver).input_user_data_in_field()
    UserPage(driver).click_privacy_and_continue_for_registration()
    UserPage(driver).checking_registration()


@pytest.mark.xfail(reason='Предусмотрите снятие скриншота и добавление его в отчёт при падении тестов.')
@UserPage.check_test
@allure.step('Тест на добавление скрина при фейле')
def test_fail(driver, base_url):
    UserPage(driver)._open_url(url=f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver).click_privacy_and_continue_for_registration()
    UserPage(driver).checking_registration()
