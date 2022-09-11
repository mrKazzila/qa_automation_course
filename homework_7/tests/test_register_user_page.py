from homework_6.pages.UserPage import UserPage


def test_register_page_title(driver, base_url):
    driver.get(f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_title_contain(UserPage.TITLE)


def test_register_page_name_field(driver, base_url):
    driver.get(f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_element(UserPage.FIRST_NAME_FIELD)


def test_register_page_subscribe_btn(driver, base_url):
    driver.get(f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_element(UserPage.SUBSCRIBE_BTN)


def test_register_page_continue_btn(driver, base_url):
    driver.get(f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_element(UserPage.CONTINUE_BUTTON)


def test_register_page_privacy_checkbox_btn(driver, base_url):
    driver.get(f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver)._wait_element(UserPage.PRIVACY_CHECKBOX_BTN)


def test_registration_new_user(driver, base_url):
    driver.get(f'{base_url}{UserPage.ADD_URL}')
    UserPage(driver).input_user_data_in_field()
    UserPage(driver).click_privacy_and_continue_for_registration()
    UserPage(driver).checking_registration()
