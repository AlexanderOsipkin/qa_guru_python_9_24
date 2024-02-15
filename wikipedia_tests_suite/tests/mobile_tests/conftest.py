import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser
from settings import user_credentials
from utils import attach
import os


@pytest.fixture(scope='function', autouse=True)
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities(
        {
            "platformVersion": "12.0",
            "deviceName": "Samsung Galaxy S21",
            "app": "bs://sample.app",
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": user_credentials.user_name,
                "accessKey": user_credentials.access_key,
            },
        }
    )

    browser.config.driver = webdriver.Remote(
        user_credentials.remote_url, options=options
    )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_bstack_video(browser)

    browser.quit()
