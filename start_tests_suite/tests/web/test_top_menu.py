import allure
from start_tests_suite.pages.web.base_page import base_page


@allure.epic('Base page')
@allure.story('Films button')
@allure.title('Films button should be work')
@allure.feature('Films button')
@allure.label('microservice', 'base page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_films_button():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Нажать на кнопку Фильмы"):
        base_page.click_on_films_button()
    with allure.step("Проверяем что заголовок раздела отображается корректно"):
        base_page.films_title_should_be_visible()


@allure.epic('Base page')
@allure.story('Series button')
@allure.title('Series button should be work')
@allure.feature('Series button')
@allure.label('microservice', 'base page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_series_button():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Нажать на кнопку Сериалы"):
        base_page.click_on_series_button()
    with allure.step("Проверяем что заголовок раздела отображается корректно"):
        base_page.series_title_should_be_visible()


@allure.epic('Base page')
@allure.story('Animation button')
@allure.title('Animation button should be work')
@allure.feature('Animation button')
@allure.label('microservice', 'base page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_animation_button():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Нажать на кнопку Мультфильмы"):
        base_page.click_on_animation_button()
    with allure.step("Проверяем что заголовок раздела отображается корректно"):
        base_page.animation_title_should_be_visible()


@allure.epic('Base page')
@allure.story('New button')
@allure.title('New button should be work')
@allure.feature('New button')
@allure.label('microservice', 'base page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_new_button():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Нажать на кнопку Новинки"):
        base_page.click_on_new_button()
    with allure.step("Проверяем что заголовок раздела отображается корректно"):
        base_page.new_title_should_be_visible()
