from src.views.login_view import LoginViewLocator


def test_create_project(driver, create_project):
    project_name = create_project
    login_view = LoginViewLocator(driver)
    login_view.click_on_continue_with_email()
