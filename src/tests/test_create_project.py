import src.requests.todoist_requests as td
from src.views.login_view import LoginViewLocator


def test_create_project(driver):
    td.create_project(name='random')
    login_view = LoginViewLocator(driver)
    login_view.click_on_continue_with_email()
