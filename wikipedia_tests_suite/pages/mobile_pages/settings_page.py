from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class SettingsPage:
    title_settings = (AppiumBy.CLASS_NAME, 'android.widget.TextView')
    button_return = (AppiumBy.CLASS_NAME, 'android.widget.ImageButton')

    def assert_open(self):
        browser.all(self.title_settings).element_by(have.text('Settings')).should(
            be.visible
        )

    def button_return_click(self):
        browser.element(self.button_return).click()


settings_page = SettingsPage()
