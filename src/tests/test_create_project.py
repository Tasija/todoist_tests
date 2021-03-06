from src.views.login_view import LoginView

EMAIL = 'bulatova_a@ukr.net'
PASSWORD = 'g9ke6p3FuSM3iDb'


def test_create_project(delete_all_projects, create_project, driver):
    # Clean up env before test
    delete_all_projects
    # Init Views
    login_view = LoginView(driver)
    # Step 1 Create test project via API.
    project_name, project_id = create_project
    # Step 2 Login into mobile application.
    main_view = login_view.do_login(EMAIL, PASSWORD)
    # Step 3 Verify on mobile that project is created
    main_view.change_current_view()
    main_view.click_on_expand_collapse_projects()
    assert main_view.find_project_by_name(project_name), 'Project does not exist'
