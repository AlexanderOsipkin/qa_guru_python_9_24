from selene import browser, have


def test_kinopoisk():
    browser.open("https://hd.kinopoisk.ru/")
    browser.element('[data-tid="SearchButton"]').type("большой куш")
    browser.element("#suggest-item-0").click()
    browser.element(
        ".ContentWrapper_content__J_a5d " ".ContentOverview_description__taSkF"
    ).should(
        have.text(
            "Набитая деньгами сумка влияет на жизни разных ушлых нищебродов. Корейский триллер в духе братьев Коэн"
        )
    )
