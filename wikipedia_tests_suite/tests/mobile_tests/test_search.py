import allure
from wikipedia_tests_suite.pages.mobile_pages.main_page import main_page
from wikipedia_tests_suite.pages.mobile_pages.search_results_page import search_results


@allure.title('Search title should be shown')
@allure.epic('Search field')
@allure.story('Search field')
@allure.feature('Search field')
@allure.label('microservice', 'Search field')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_search():
    with allure.step('Выполняем поиск'):
        main_page.search('Sherlock Holmes')
    with allure.step('Выполняем проверку результатов поиска'):
        search_results.assert_results_exist()


@allure.title('Main page should be shown')
@allure.epic('Main page')
@allure.story('Main page')
@allure.feature('Main page')
@allure.label('microservice', 'Main page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'mobile', 'critical')
@allure.severity('critical')
@allure.label('layer', 'mobile')
def test_return_to_main_page_from_search_results():
    with allure.step('Выполняем поиск'):
        main_page.search('Sherlock Holmes')
    with allure.step('Нажимаем кнопку возврата на предыдущую страницу'):
        search_results.button_return_click()
    with allure.step('Выполняем проверку заголовка на главной странице'):
        main_page.assert_title()
