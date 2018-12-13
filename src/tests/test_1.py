import src.requests.todoist_requests as td


def test_create_project(driver):
    td.create_project(name='random')
