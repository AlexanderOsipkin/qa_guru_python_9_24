import allure
from wikipedia_tests_suite.pages.web_pages.searh_field import search_field
from wikipedia_tests_suite.pages.web_pages.base_page import base_page


@allure.epic('Search')
@allure.story('Find article')
@allure.title('Find article by title')
@allure.feature('Search')
@allure.label('microservice', 'Search')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
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
    with allure.step("Нажимаем на поле ввода"):
        search_field.click_on_search_field()
    with allure.step("Вводим название статьи"):
        search_field.type_article_title("Александр Сергеевич Пушкин")
    with allure.step("Проверяем что открыли верную страницу"):
        search_field.article_title_should_be_visible()
