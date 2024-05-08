import os
import pytest
from allure import step
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
from project import config
from utils import attach

DEFAULT_PLATFORM = "android"


@pytest.fixture(scope="function", params=["android", "ios"])
def mobile_management(request):
    platform = request.param if request.param is not None else DEFAULT_PLATFORM
    if platform == "android":
        options = UiAutomator2Options().load_capabilities({
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": config.app,
            'bstack:options': {
                "projectName": "Bstack_SergeyG_android_test",
                "buildName": "android_browserstack-test-build",
                "sessionName": "Android Browserstack test session",
                "userName": config.user,
                "accessKey": config.access_key
            }
        })
    elif platform == "ios":
        options = XCUITestOptions().load_capabilities({
            "platformName": "ios",
            "platformVersion": "15.0",
            "deviceName": "iPhone 13",
            "app": config.app,
            'bstack:options': {
                "projectName": "Bstack_SergeyG_ios_test",
                "buildName": "ios_browserstack-test-build",
                "sessionName": "iOS Browserstack test session",
                "userName": config.user,
                "accessKey": config.access_key
            }
        })
    with step("Setting up Browserstack remote executor"):
        browser.config.driver = webdriver.Remote(config.bstack_url, options=options)
    with step("Setting up timeout for browser"):
        browser.config.timeout = 30.0

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()
