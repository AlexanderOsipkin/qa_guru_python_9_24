import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': '100.0',
        'selenoid:options': {'enableVNC': True, 'enableVideo': True},
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    remote_browser_url = os.getenv('REMOTE_BROWSER_URL')

    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@{remote_browser_url}',
        options=options,
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://start.ru/'
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


# @pytest.fixture(scope='function', autouse=True)
# def browser_cfg():
#     browser.config.base_url = 'https://start.ru/'
#     driver_options = webdriver.ChromeOptions()
#     browser.config.driver_options = driver_options
#     browser.config.timeout = 15
#     browser.config.window_height = 1080
#     browser.config.window_width = 1920
#
#     yield
#
#     browser.quit()
