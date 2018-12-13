import todoist

API_TOKEN = 'f2d539eb6f1a5c08d21dc196583c37d43df3295e'


def create_project(name):
    api = todoist.TodoistAPI(API_TOKEN)
    project = api.projects.add(name)
    api.commit()
