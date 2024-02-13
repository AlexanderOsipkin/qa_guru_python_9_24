import allure
from start_tests_suite.pages.web.search_field import search_field


import allure
from kinopoisk_tests_suite.pages.web.serach_field import search


@allure.epic('Search')
@allure.story('Find movie')
@allure.title('Find movie by title')
@allure.feature('Search')
@allure.label('microservice', 'Search')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_find_movie_by_title():
    with allure.step("Открываем главную страницу"):
        search_field.open_main_page()
    with allure.step("Нажать на кнопку поиска"):
        search_field.click_on_search_button()
    with allure.step("Ввести название фильма"):
        search_field.type_movie_title("Олдбой")
    with allure.step("Проверяем выбранный фильм на соответствие"):
        search_field.selected_movie_should_be_visible()
