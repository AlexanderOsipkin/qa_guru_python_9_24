from selene import browser, have, be


class TestSearch:
    def open_main_page(self):
        browser.open("/")
        return self

    def click_on_search_button(self):
        browser.element('[data-testid="search_loupe"]').should(be.visible).click()
        return self

    def type_movie_title(self, value):
        browser.element('.HeaderSearch_header-search__input-text__F3SjJ').type(
            value
        ).press_enter()
        return self

    def selected_movie_should_be_visible(self):
        browser.element(
            '.VideoUnit_vline__slider__card__title__MoZVS .VideoUnit_title__J_lZy'
        ).should(have.text('Трактат о бабочках'))
        return self


search_field = TestSearch()
