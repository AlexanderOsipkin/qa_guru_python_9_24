from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


class MainPage:
    field_search_init = (AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')
    field_search_do = (AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')
    button_action_menu = (AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button')
    button_settings = (AppiumBy.ID, 'org.wikipedia.alpha:id/explore_overflow_settings')
    title = (AppiumBy.ID, 'org.wikipedia.alpha:id/single_fragment_toolbar_wordmark')

    def search(self, value):
        browser.element(self.field_search_init).click()
        browser.element(self.field_search_do).type(value)

    def open_action_menu(self):
        browser.element(self.button_action_menu).click()

    def open_settings(self):
        browser.element(self.button_settings).click()

    def assert_title(self):
        browser.element(self.title).should(be.visible)


main_page = MainPage()
