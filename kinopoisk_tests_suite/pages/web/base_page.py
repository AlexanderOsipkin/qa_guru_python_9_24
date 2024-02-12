from selene import browser, have, be


class TestBasePage:
    def open_main_page(self):
        browser.open("/")
        return self

    def kinopoisk_top_menu_shuld_be_visible(self):
        browser.element(
            '.Footer_copyrights-row__cQ1t8 .Footer_copyrights-rec__uSCFM .Link_root__Z3NLP'
        ).should(have.text('Кинопоиск'))
        return self

    def click_on_watching_now(self):
        browser.element(
            '.content-section__item:nth-child(2) .ListHeader_title__MmKl_'
        ).should(be.visible).click()
        return self

    def title_should_be_visible(self):
        browser.element('.FilmList_root__62ABh .Text_root__A9RJ2').should(
            have.text("Смотрят сейчас")
        )
        return self

    def click_on_main_content_button(self):
        browser.element('#subscriptions').should(be.visible).click()
        browser.element(
            '.Footer_copyrights-row__cQ1t8 .Footer_copyrights-rec__uSCFM .Link_root__Z3NLP'
        ).should(have.text('Кинопоиск'))
        return self

    def check_promo_title(self):
        browser.element('.styles_content__T7B3K .style_button__PNtXT').should(
            have.text('Попробовать 30 дней бесплатно')
        )
        return self

    def check_promo_button(self):
        browser.element('.styles_content__T7B3K .style_button__PNtXT').should(
            be.visible
        ).click()
        browser.element('.passp-add-account-page-title').should(
            have.text('Войдите или зарегистрируйтесь')
        )
        return self


kinopoisk = TestBasePage()
