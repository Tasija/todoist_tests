from src.views.base_page import BasePage
from src.views.task_view import TaskView
from src.views.locators import Locators


class MainView(BasePage):

    def click_on_expand_collapse_projects(self):
        self.wait_until_element_appear(Locators.project_expand_collaps_btn).click()

    def click_on_project(self, name):
        project = self.find_project_by_name(name)
        project.click()
        return TaskView(self.driver)

    def find_project_by_name(self, name):
        return self.wait_until_element_appear(Locators.project_name(name))
