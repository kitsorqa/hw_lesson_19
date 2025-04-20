from allure_commons._allure import step
from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy


def test_search_appium_android(mobile_management):
    with step("Клик по кнопке Пропустить"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    with step("Ввод в поле поиска слово Appium"):
        browser.element(("accessibility id", "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with step("Получение результата и его сравнение"):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

    with step("Открытие страницы Appium"):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.first.click()

def test_skip_main_screens(mobile_management):
    with step("Запуск первого приветственного экрана и его проверка"):
        with step("Проверка текста на первом экране"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("The Free Encyclopedia"))
        with step("Проверка наличия кнопки Пропустить"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_pager")).should(be.clickable)
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with step("Запуск второго экрана и его проверка"):
        with step("Проверка наличия кнопки Пропустить"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).should(be.clickable)
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with step("Запуск третьего экрана и его проверка"):
        with step("Проверка наличия кнопки Пропустить"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).should(be.clickable)
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with step("Запуск четвертого экрана и его проверка"):
        with step("Проверка отсутствия кнопки Пропустить"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).should(be.not_.present)
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).should(be.clickable).click()

    with step("Проверка главного экрана"):
        with step("Наличие отображения Wikipedia в хедере страницы"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/main_toolbar_wordmark")).should(be.visible)