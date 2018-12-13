import os
import pytest
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '9'


@pytest.fixture()
def driver(request):
    desired_caps = {'platformName': 'Android',
                    'platformVersion': PLATFORM_VERSION,
                    'automationName': 'uiautomator2',
                    'deviceName': 'Nexus 5X API 28',
                    'app-package': 'com.todoist',
                    'appWaitActivity': 'com.todoist.activity.*',
                    'app': '/Users/tasijafox/PycharmProjects/todoist/Todoist_v12.8_apkpure.com.apk',
                    'autoGrantPermissions': 'true'}
    driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver


@pytest.fixture()
def do_login(driver):
    driver.find_element()