import allure
from kinopoisk_tests_suite.pages.web.serach_field import search


@allure.epic('Search')
@allure.story('Find_movie')
@allure.title('Find_movie_by_title')
@allure.feature('Search')
@allure.label('microservice', 'Search')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_find_movie_by_title():
    with allure.step("Открываем главную страницу"):
        search.open_main_page()
    with allure.step("Нажать на кнопку поиска"):
        search.click_on_search()
    with allure.step("Ввести название фильма"):
        search.type_movie_title("Большой куш")
    with allure.step("Выбрать нужный фильм из списка"):
        search.select_movie_in_list()
    with allure.step("Проверяем выбранный фильм на соответствие"):
        search.selected_movie_should_be_visible()