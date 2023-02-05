import json
import logging
import os

import allure
import pytest
from selenium import webdriver

drivers = os.path.expanduser('drivers')


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--executor', action='store', default='192.168.0.179')
    parser.addoption('--vnc', action='store_true', default=False)
    parser.addoption('--logs', action='store_true', default=False)
    parser.addoption('--video', action='store_true', default=True)
    parser.addoption('--url', action='store', default='http://192.168.0.179:8081/')
    parser.addoption('--bversion')


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def driver(request):

    driver = request.config.getoption('--browser')
    vnc = request.config.getoption('--vnc')
    logs = request.config.getoption('--logs')
    video = request.config.getoption('--video')
    version = request.config.getoption('--bversion')
    executor = request.config.getoption('--executor')

    executor_url = f'http://{executor}:4444/wd/hub'

    # fix bug with dict https://github.com/operasoftware/operachromiumdriver/issues/96#issuecomment-985291083
    options = webdriver.ChromeOptions()
    if driver == 'opera':
        options.add_experimental_option('w3c', True)

    if executor == 'local':
        if driver == 'chrome':
            browser = webdriver.Chrome(executable_path=f'{drivers}/chromedriver')
        elif driver == 'firefox':
            browser = webdriver.Firefox(executable_path=f'{drivers}/geckodriver')
        elif driver == 'opera':
            browser = webdriver.Opera(
                executable_path=f'{drivers}/operadriver',
                options=options,
            )
        else:
            raise ValueError(f'Browser {driver} not supported!')
    else:
        capabilities = {
            'browserName': driver,
            'browserVersion': version,
            'selenoid:options': {
                'enableVNC': vnc,
                'enableVideo': video,
                'enableLog': logs,
            },
            'name': 'OtusQAPython',
        }

        browser = webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=executor_url,
            options=options,
        )

    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.capabilities),
        attachment_type=allure.attachment_type.JSON,
    )

    def finalizer():
        browser.quit()
        with open('allure-results/environment.xml', 'w+') as file:
            file.write(
                f"""<environment>
                        <parameter>
                            <key>Browser</key>
                            <value>{browser}</value>
                        </parameter>
                        <parameter>
                            <key>Browser.Version</key>
                            <value>{version}</value>
                        </parameter>
                        <parameter>
                            <key>Executor</key>
                            <value>{executor_url}</value>
                        </parameter>
                    </environment>
                    """,
            )

    browser.maximize_window()

    browser.test_name = request.node.name
    browser.log_level = logging.DEBUG

    request.addfinalizer(finalizer)

    return browser
