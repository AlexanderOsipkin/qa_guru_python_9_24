from selene import browser, have, be


class TestSearch:
    def open_main_page(self):
        browser.open("/")
        return self

    def click_on_search(self):
        browser.element('[data-tid="SearchButton"]').should(be.visible).click()
        return self

    def type_movie_title(self, value):
        browser.element('[role="searchbox"]').type(value).press_enter()
        return self

    def select_movie_in_list(self):
        browser.element('#suggest-item-0').click()
        return self

    def selected_movie_should_be_visible(self):
        browser.element(
            '.ContentWrapper_content__J_a5d .ContentOverview_description__taSkF'
        ).should(
            have.text(
                'Набитая деньгами сумка влияет на жизни разных ушлых нищебродов. Корейский триллер в духе братьев Коэн'
            )
        )
        return self


search = TestSearch()
