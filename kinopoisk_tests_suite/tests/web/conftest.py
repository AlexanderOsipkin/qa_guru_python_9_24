import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_cfg():
    browser.config.base_url = 'https://hd.kinopoisk.ru/'
    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.timeout = 15
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()
