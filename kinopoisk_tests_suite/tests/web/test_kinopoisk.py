import allure
from kinopoisk_tests_suite.pages.web.base_page import kinopoisk


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
        kinopoisk.open_main_page()
    with allure.step("Кинопоиск - отображается в футоре страницы"):
        kinopoisk.kinopoisk_top_menu_shuld_be_visible()


@allure.story('Watching now button')
@allure.title('Button should be work')
@allure.feature('Watching now')
@allure.label('microservice', 'base page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_watching_now_button():
    with allure.step("Открыть главную страницу"):
        kinopoisk.open_main_page()
    with allure.step("Нажать на кнопку смотрят сейчас"):
        kinopoisk.click_on_watching_now()
    with allure.step("Заголовок раздела - отображается на странице"):
        kinopoisk.title_should_be_visible()


@allure.story('Open promo page')
@allure.title('Promo page should be shown')
@allure.feature('Promo page')
@allure.label('microservice', 'Promo page')
@allure.label('owner', 'allure8')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
def test_open_promo_page():
    with allure.step("Открыть главную страницу"):
        kinopoisk.open_main_page()
    with allure.step("Проверяем заголовок промо акции"):
        kinopoisk.check_promo_title()
    with allure.step("Проверяем кнопку промо акции"):
        kinopoisk.check_promo_button()
