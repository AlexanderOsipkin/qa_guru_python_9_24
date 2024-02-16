import allure
from wikipedia_tests_suite.pages.web_pages.base_page import base_page


@allure.epic('Base page')
@allure.story('Content button')
@allure.title('Content button should be work')
@allure.feature('Content button')
@allure.label('microservice', 'base page')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_content_button():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.wikipedia_logo_should_be_visible()
    with allure.step("Переходим в ru раздел wikipedia"):
        base_page.go_to_ru_wikipedia()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.title_should_be_visible()
    with allure.step("Нажимаем на кнопку - содержание"):
        base_page.click_on_content_button()
    with allure.step("Проверяем заголовок страницы"):
        base_page.content_title_should_be_visible()


@allure.epic('Base page')
@allure.story('Featured button')
@allure.title('Featured button should be work')
@allure.feature('Featured button')
@allure.label('microservice', 'base page')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_featured_button():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.wikipedia_logo_should_be_visible()
    with allure.step("Переходим в ru раздел wikipedia"):
        base_page.go_to_ru_wikipedia()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.title_should_be_visible()
    with allure.step("Нажимаем на кнопку - избранные статьи"):
        base_page.click_on_featured_button()
    with allure.step("Проверяем заголовок страницы"):
        base_page.featured_title_should_be_visible()


@allure.epic('Base page')
@allure.story('Randompage button')
@allure.title('Randompage button should be work')
@allure.feature('Randompage button')
@allure.label('microservice', 'base page')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_randompage_button():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.wikipedia_logo_should_be_visible()
    with allure.step("Переходим в ru раздел wikipedia"):
        base_page.go_to_ru_wikipedia()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.title_should_be_visible()
    with allure.step("Нажимаем на кнопку - случайная статья"):
        base_page.click_on_randompage_button()
    with allure.step("Проверяем заголовок страницы"):
        base_page.randompage_title_should_be_visible()


@allure.epic('Base page')
@allure.story('Currentevents button')
@allure.title('Currentevents button should be work')
@allure.feature('Currentevents button')
@allure.label('microservice', 'base page')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_currentevents_button():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.wikipedia_logo_should_be_visible()
    with allure.step("Переходим в ru раздел wikipedia"):
        base_page.go_to_ru_wikipedia()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.title_should_be_visible()
    with allure.step("Нажимаем на кнопку - текущие события"):
        base_page.click_on_currentevents_button()
    with allure.step("Проверяем заголовок страницы"):
        base_page.currentevents_title_should_be_visible()


@allure.epic('Base page')
@allure.story('Sitesupport button')
@allure.title('Sitesupport button should be work')
@allure.feature('Sitesupport button')
@allure.label('microservice', 'base page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_sitesupport_button():
    with allure.step("Открыть главную страницу"):
        base_page.open_main_page()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.wikipedia_logo_should_be_visible()
    with allure.step("Переходим в ru раздел wikipedia"):
        base_page.go_to_ru_wikipedia()
    with allure.step("Проверяем что открыли верную страницу"):
        base_page.title_should_be_visible()
    with allure.step("Нажимаем на кнопку - пожертвовать"):
        base_page.click_on_sitesupport_button()
