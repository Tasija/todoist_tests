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

    def click_on_task(self, name):
        self.driver.find_element(*Locators.item_name(name)).click()

    def click_on_complete_task_btn(self):
        self.driver.find_element(*Locators.complete_task_btn).click()
        self.wait_until_element_appear(Locators.add_task_btn)

    def complete_task(self, name):
        self.click_on_task(name)
        self.click_on_complete_task_btn()

    def is_task_un_completed(self, task_name):
        if self.driver.find_elements(*Locators.item_name(task_name)):
            return True
        return False
