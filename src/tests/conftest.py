import os
import pytest
import string
import random
from appium import webdriver
import src.requests.todoist_requests as td
from src.views.login_view import LoginView

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
    login_view = LoginView(driver)
    login_view.click_on_continue_with_email()
    login_view.set_email('bulatova_a@ukr.net')
    login_view.click_on_continue_with_email_next()
    login_view.wait_until_progress_bar_disappear()
    login_view.set_password('g9ke6p3FuSM3iDb')
    login_view.click_log_in()


@pytest.fixture()
def create_project():
    name = name_generator()
    td.create_project(name)
    return name
