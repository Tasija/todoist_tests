from src.views.login_view import LoginView
import src.requests.todoist_requests as td

EMAIL = 'bulatova_a@ukr.net'
PASSWORD = 'g9ke6p3FuSM3iDb'


def test_create_project(delete_all_projects, create_project, driver):
    NEW_TASK_NAME = "New Task Name"
    # Clean up env before test
    delete_all_projects
    # Step 1 Create test task via mobile application in test project
    # Init Views
    login_view = LoginView(driver)
    project_name, project_id = create_project
    main_view = login_view.do_login(EMAIL, PASSWORD)
    main_view.change_current_view()
    main_view.click_on_expand_collapse_projects()
    task_view = main_view.click_on_project(project_name)
    task_view.create_new_task(NEW_TASK_NAME)
    all_tasks_names = td.find_all_tasks_names_via_api()
    assert NEW_TASK_NAME in all_tasks_names, 'Task Name does not exist'
