import allure
from wikipedia_tests_suite.pages.mobile_pages.settings_page import settings_page
from wikipedia_tests_suite.pages.mobile_pages.main_page import main_page


@allure.title('Settings page should be shown')
@allure.epic('Settings page')
@allure.story('Settings page')
@allure.feature('Settings page')
@allure.label('microservice', 'Settings page')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('smoke', 'regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_open_settings():
    with allure.step('Открываем меню действий'):
        main_page.open_action_menu()
    with allure.step('Выбираем в меню пункт Settings'):
        main_page.open_settings()
    with allure.step('Проверяем, что открылась страница Settings'):
        settings_page.assert_open()


@allure.title('Settings page should be shown')
@allure.epic('Settings page')
@allure.story('Settings page')
@allure.feature('Settings page')
@allure.label('microservice', 'Settings page')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('smoke', 'regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_return_to_main_page_from_settings():
    with allure.step('Открываем меню действий'):
        main_page.open_action_menu()
    with allure.step('Выбираем в меню пункт Settings'):
        main_page.open_settings()
    with allure.step('Нажимаем кнопку возврата на предыдущую страницу'):
        settings_page.button_return_click()
    with allure.step('Выполняем проверку заголовка на главной странице'):
        main_page.assert_title()
