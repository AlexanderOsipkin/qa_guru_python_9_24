import allure
from start_tests_suite.pages.web.base_page import base_page


@allure.epic('Base_page')
@allure.story('Open_base_page')
@allure.title('Base_page_should_be_shown')
@allure.feature('Base_page')
@allure.label('microservice', 'Base page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_base_page():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.start_should_be_visible()


@allure.epic('Base page')
@allure.story('Open promo page')
@allure.title('Promo page should be shown')
@allure.feature('Promo page')
@allure.label('microservice', 'Promo page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_open_promo_page():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Проверяем заголовок промо акции"):
        base_page.check_promo_title()
    with allure.step("Проверяем кнопку промо акции"):
        base_page.check_promo_button()
