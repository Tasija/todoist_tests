from src.views.base_page import BasePage
from src.views.locators import Locators


class TaskView(BasePage):

    def click_on_add_task_button(self):
        self.driver.find_element(*Locators.add_task_btn).click()

    def set_task_name(self, name):
        self.driver.find_element(*Locators.task_name_field).send_keys(name)

    def hit_enter_task_name(self):
        self.driver.find_element(*Locators.enter_task).click()

    def create_new_task(self, name):
        self.click_on_add_task_button()
        self.set_task_name(name)
        self.hit_enter_task_name()
        self.change_current_view()
