import allure
from wikipedia_tests_suite.pages.web_pages.base_page import base_page


@allure.epic('Base page')
@allure.story('Open base page')
@allure.title('Base page should be shown')
@allure.feature('Base page')
@allure.label('microservice', 'Base page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_base_page():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.wikipedia_logo_should_be_visible()
    with allure.step("Переходим в ru раздел wikipedia"):
        base_page.go_to_ru_wikipedia()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.title_should_be_visible()
