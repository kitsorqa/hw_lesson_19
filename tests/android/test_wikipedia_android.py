from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy


def test_search_appium_android(android_management):
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Appium")
    results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
    results.should(have.size_greater_than(0))
    results.first.should(have.text("Appium")).click()


def test_search_python_android(android_management):
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Python")
    results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
    results.should(have.size_greater_than(0))
    results.second.should(have.text("Python (programming language)")).click()
