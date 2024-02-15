from selene import browser, have, be


class TestSearch:
    def click_on_search_field(self):
        browser.element('[id="searchInput"]').should(be.visible).click()
        return self

    def type_article_title(self, value):
        browser.element('[id="searchInput"]').type(value).press_enter()
        return self

    def article_title_should_be_visible(self):
        browser.element('.infobox-above').should(
            have.text('Александр Сергеевич Пушкин')
        )
        return self


search_field = TestSearch()
