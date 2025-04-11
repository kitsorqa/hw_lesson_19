import logging
import os

import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selenium import webdriver
from selene import browser
from dotenv import load_dotenv


def general_settings(options):
    browser.config.driver = webdriver.Remote('http://hub.browserstack.com/wd/hub', options=options)
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def get_creeds():
    USERNAME = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    logging.info(USERNAME)
    logging.info(PASSWORD)
    return USERNAME, PASSWORD


@pytest.fixture(scope='function')
def android_management():
    creeds = get_creeds()
    USERNAME = creeds[0]
    PASSWORD = creeds[1]

    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": USERNAME,
            "accessKey": PASSWORD
        }
    })

    general_settings(options)

    yield

    browser.quit()


@pytest.fixture(scope='function')
def ios_management():
    creeds = get_creeds()
    USERNAME = creeds[0]
    PASSWORD = creeds[1]

    options = XCUITestOptions().load_capabilities({
        # Set URL of the application under test
        "app": "bs://sample.app",

        # Specify device and os_version for testing
        "deviceName": "iPhone 14 Pro",
        "platformName": "ios",
        "platformVersion": "16",

        # Set other BrowserStack capabilities
        "bstack:options": {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": USERNAME,
            "accessKey": PASSWORD
        }
    })

    general_settings(options)

    yield

    browser.quit()
