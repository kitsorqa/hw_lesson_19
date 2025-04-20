import allure
import pytest
from selene import browser
from appium import webdriver
from config import config

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = config.get_options()
    browser.config.driver = webdriver.Remote(
        config.remote_url,
        options = options
    )
    browser.config.timeout = config.timeout

    yield

    attach.attach_screenshot()
    attach.attach_xml_logs()

    session_id = browser.driver.session_id
    browser.quit()
    if config.context == 'bstack':
        attach.bstack_video(session_id)