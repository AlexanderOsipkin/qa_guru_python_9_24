from selene import browser, have, be


class TestBasePage:
    def open_main_page(self):
        browser.open("/")
        return self

    def start_should_be_visible(self):
        browser.element(
            '.Footer_footer__item-apps__dPbHI .Footer_footer__item-title__aONEj'
        ).should(have.text('START на большом экране'))
        return self

    def click_on_films_button(self):
        browser.element('[data-testid="movies_button"]').should(be.visible).click()
        return self

    def films_title_should_be_visible(self):
        browser.element('.Catalog_page_wrapper__yaWms .Catalog_catalog__Gjv4a').should(
            have.text("Фильмы смотреть онлайн")
        )
        return self

    def click_on_series_button(self):
        browser.element('[data-testid="series_button"]').should(be.visible).click()
        return self

    def series_title_should_be_visible(self):
        browser.element('.Catalog_page_wrapper__yaWms .Catalog_catalog__Gjv4a').should(
            have.text("Сериалы смотреть онлайн")
        )
        return self

    def click_on_animation_button(self):
        browser.element('[data-testid="animation_button"]').should(be.visible).click()
        return self

    def animation_title_should_be_visible(self):
        browser.element('.Catalog_page_wrapper__yaWms .Catalog_catalog__Gjv4a').should(
            have.text("Мультфильмы смотреть онлайн")
        )
        return self

    def click_on_new_button(self):
        browser.element('[data-testid="new_button"]').should(be.visible).click()
        return self

    def new_title_should_be_visible(self):
        browser.element(
            '.Genres_new_wrapper__lzxBE .Genres_genres_global_body__LutVL'
        ).should(have.text("Новинки фильмов, мультфильмов и сериалов смотреть онлайн"))
        return self

    def check_promo_title(self):
        browser.element('[data-testid="try_free_button_text"]').should(
            have.text('Попробовать бесплатно')
        )
        return self

    def check_promo_button(self):
        browser.element('[data-testid="try_free_button_text"]').should(
            be.visible
        ).click()
        browser.element('[data-testid="payment_button_text"]').should(
            have.text('Зарегистрироваться')
        )
        return self


base_page = TestBasePage()
