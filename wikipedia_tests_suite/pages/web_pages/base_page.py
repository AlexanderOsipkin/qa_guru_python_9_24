from selene import browser, have, be


class TestBasePage:
    def open_main_page(self):
        browser.open("/")
        return self

    def wikipedia_logo_should_be_visible(self):
        browser.element('.central-textlogo-wrapper .central-textlogo__image').should(
            have.text('Wikipedia')
        )
        return self

    def go_to_ru_wikipedia(self):
        browser.element('#js-link-box-ru').should(be.visible).click()
        return self

    def title_should_be_visible(self):
        browser.element('.main-top-header .mw-headline').should(
            have.text("Добро пожаловать в")
        )
        return self

    def click_on_content_button(self):
        browser.element('#n-content').should(be.visible).click()
        return self

    def content_title_should_be_visible(self):
        browser.element('.mw-page-title-main').should(have.text("Содержание"))
        return self

    def click_on_featured_button(self):
        browser.element('#n-featured').should(be.visible).click()
        return self

    def featured_title_should_be_visible(self):
        browser.element('.mw-page-title-main').should(have.text("Избранные статьи"))
        return self

    def click_on_randompage_button(self):
        browser.element('#n-randompage').should(be.visible).click()
        return self

    def randompage_title_should_be_visible(self):
        browser.element('#ca-talk').should(have.text("Обсуждение"))
        return self

    def click_on_currentevents_button(self):
        browser.element('#n-currentevents').should(be.visible).click()
        return self

    def currentevents_title_should_be_visible(self):
        browser.element('.mw-page-title-main').should(have.text("Текущие события"))
        return self

    def click_on_sitesupport_button(self):
        browser.element('#n-sitesupport').should(be.visible).click()
        return self

    def sitesupport_title_should_be_visible(self):
        browser.element('.col-2:nth-child(2) > p:nth-child(1)').should(
            have.text(
                "Благодарим вас за ваш интерес к поддержке Фонда Викимедиа. К сожалению, в настоящий момент мы не можем принимать пожертвования из России. Мы ценим вашу поддержку, ибо наша цель – нести знания в каждый уголок мира."
            )
        )
        return self


base_page = TestBasePage()
