from selene import browser, have, be


class TopMenu:
    def open_main_page(self):
        browser.open("/")
        return self

    def click_on_channels_button(self):
        browser.element('#channels').should(be.visible).click()
        return self

    def check_channels_title(self):
        browser.element('.ContentPageLayout_root__Iol6N .Text_root__A9RJ2').should(
            have.text('Смотреть каналы')
        )
        return self

    def click_on_sport_button(self):
        browser.element('.NavLink_root__OtAfX .Link_root__Z3NLP').should(
            be.visible
        ).click()
        return self

    def check_sport_title(self):
        browser.element('.competitions-carousel_header__XIvLq').should(
            have.text('Лиги и чемпионаты')
        )
        return self

    def click_on_games_button(self):
        browser.element('#games').should(be.visible).click()
        return self

    def check_games_title(self):
        browser.element(
            '.GamesPaywall_headline__wx4Tv .GamesPaywall_title__IEPvy'
        ).should(have.text('Весёлые игры для большой компании'))
        return self


top_menu = TopMenu()
