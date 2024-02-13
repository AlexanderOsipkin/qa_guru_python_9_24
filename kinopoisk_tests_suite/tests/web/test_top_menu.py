import allure
from kinopoisk_tests_suite.pages.web.top_menu import top_menu


@allure.epic('Top menu')
@allure.story('Open channels page')
@allure.title('Channels page should be shown')
@allure.feature('channels page')
@allure.label('microservice', 'channels page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_channels():
    with allure.step("Открыть главную страницу"):
        top_menu.open_main_page()
    with allure.step('Нажать на кнопку "Каналы"'):
        top_menu.click_on_channels_button()
    with allure.step('Проверяем заголовок "Каналы"'):
        top_menu.check_channels_title()


@allure.epic('Top menu')
@allure.story('Open sports page')
@allure.title('Sports page should be shown')
@allure.feature('sports page')
@allure.label('microservice', 'sports page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_sports():
    with allure.step("Открыть главную страницу"):
        top_menu.open_main_page()
    with allure.step('Нажать на кнопку "Спорт"'):
        top_menu.click_on_sport_button()
    with allure.step('Проверяем заголовок "Спорт"'):
        top_menu.check_sport_title()


@allure.epic('Top menu')
@allure.story('Open games page')
@allure.title('Games page should be shown')
@allure.feature('games page')
@allure.label('microservice', 'games page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_games():
    with allure.step("Открыть главную страницу"):
        top_menu.open_main_page()
    with allure.step('Нажать на кнопку "Игры"'):
        top_menu.click_on_games_button()
    with allure.step('Проверяем заголовок "Игры"'):
        top_menu.check_games_title()
