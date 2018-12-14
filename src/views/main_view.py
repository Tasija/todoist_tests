from src.views.base_page import BasePage
from src.views.locators import Locators


class MainView(BasePage):

    def click_on_more_button(self):
        self.wait_until_element_appear(Locators.more_btn).click()

    def click_on_expand_collapse_projects(self):
        self.wait_until_element_appear(Locators.project_expand_collaps_btn).click()

    def get_all_projects_names(self):
        projects_list = []
        all_prjs = self.driver.find_elements(*Locators.project_name)
        for project in all_prjs:
            projects_list.append(project.text)
        return projects_list
