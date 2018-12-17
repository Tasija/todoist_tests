from src.views.login_view import LoginView
import src.requests.todoist_requests as td

EMAIL = 'bulatova_a@ukr.net'
PASSWORD = 'g9ke6p3FuSM3iDb'


def test_create_project(delete_all_projects, create_project, driver):
    NEW_TASK_NAME = "New Task Name"
    # Clean up env before test
    delete_all_projects
    # Step 1 Open mobile application
    # Init Views
    login_view = LoginView(driver)
    project_name, project_id = create_project
    main_view = login_view.do_login(EMAIL, PASSWORD)
    # Step 2 Open test project
    main_view.change_current_view()
    main_view.click_on_expand_collapse_projects()
    task_view = main_view.click_on_project(project_name)
    # Step 3 Created test task
    task_view.create_new_task(NEW_TASK_NAME)
    # Step 4 Complete test task
    task_view.complete_task(NEW_TASK_NAME)
    assert not task_view.is_task_un_completed(NEW_TASK_NAME), 'Task remains uncompleted'
    # Step 5 Reopen test task via API
    td.un_complete_task(project_id)
    # Step 6 Mobile: Verify that test task appears in your test project
    main_view.change_current_view()
    task_view = main_view.click_on_project(project_name)
    task_view.refresh_view()
    assert task_view.is_task_un_completed(NEW_TASK_NAME), 'Task remains completed'
