import todoist

API_TOKEN = 'f2d539eb6f1a5c08d21dc196583c37d43df3295e'


def create_project(name):
    api = todoist.TodoistAPI(API_TOKEN)
    project = api.projects.add(name)
    api.commit()
    return project['id']


def delete_all_project():
    api = todoist.TodoistAPI(API_TOKEN)
    all_ids = []
    for i in range(0, len(api.state['projects'])):
        all_ids.append(api.state['projects'][i]['id'])
    for id in all_ids:
        api.projects.get_by_id(id).delete()
    api.commit()


def find_all_tasks_names_via_api():
    api = todoist.TodoistAPI(API_TOKEN)
    all_names = []
    for i in range(0, len(api.state['items'])):
        all_names.append(api.state['items'][i]['content'])
    return all_names
