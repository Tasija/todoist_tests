import os
import pytest
from appium import webdriver
import src.requests.todoist_requests as td
import string
import random

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '9'


def name_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

@pytest.fixture()
def driver(request):
    desired_caps = {'platformName': 'Android',
                    'platformVersion': PLATFORM_VERSION,
                    'automationName': 'uiautomator2',
                    'deviceName': 'Nexus 5X API 28',
                    'app-package': 'com.todoist',
                    'appWaitActivity': 'com.todoist.activity.*',
                    'forceMjsonwp': 'true',
                    'app': PATH('../Todoist_v12.8_apkpure.com.apk'),
                    'autoGrantPermissions': 'true'}
    driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver


@pytest.fixture()
def do_login(driver):
    driver.find_element()


@pytest.fixture()
def create_project():
    name = name_generator()
    td.create_project(name)
    return name
