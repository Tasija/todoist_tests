from src.views.main_view import MainView
from src.views.login_view import LoginView

EMAIL = 'bulatova_a@ukr.net'
PASSWORD = 'g9ke6p3FuSM3iDb'


def test_create_project(driver, create_project):
    # Init Views
    main_view = MainView(driver)
    login_view = LoginView(driver)
    # Step 1 Create test project via API.
    project_name = create_project
    # Step 2 Login into mobile application.
    login_view.do_login(EMAIL, PASSWORD)
    # Step 3 Verify on mobile that project is created
    main_view.click_on_more_button()
    main_view.click_on_expand_collapse_projects()
    all_projects_names = main_view.get_all_projects_names()
    assert project_name in all_projects_names, 'Project does not exist'
