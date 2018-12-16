from src.views.base_page import BasePage
from src.views.locators import Locators
from src.views.main_view import MainView

class LoginView(BasePage):

    def click_on_continue_with_email(self):
        self.driver.find_element(*Locators.continue_with_email).click()

    def set_email(self, email):
        email_field = self.driver.find_element(*Locators.email_field)
        email_field.clear()
        email_field.send_keys(email)

    def click_on_continue_with_email_next(self):
        self.driver.find_element(*Locators.continue_with_email_next).click()

    def set_password(self, password):
        email_field = self.driver.find_element(*Locators.password)
        email_field.clear()
        email_field.send_keys(password)

    def click_log_in(self):
        self.driver.find_element(*Locators.log_in_btn).click()

    def do_login(self, email, password):
        self.click_on_continue_with_email()
        self.set_email(email)
        self.click_on_continue_with_email_next()
        self.wait_until_progress_bar_disappear()
        self.set_password(password)
        self.click_log_in()
        return MainView(self.driver)
