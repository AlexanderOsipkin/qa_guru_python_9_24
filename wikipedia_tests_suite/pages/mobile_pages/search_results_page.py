from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchResults:
    button_return = (AppiumBy.CLASS_NAME, 'android.widget.ImageButton')
    search_results = (AppiumBy.CLASS_NAME, 'android.widget.TextView')

    def button_return_click(self):
        browser.element(self.button_return).click()

    def assert_results_exist(self):
        browser.all(self.search_results).should(have.size_greater_than(0))


search_results = SearchResults()
