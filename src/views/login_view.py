from src.views.base_page import BasePage
from src.views.locators import Locators


class LoginViewLocator(BasePage):

    def click_on_continue_with_email(self):
        self.driver.find_element(*Locators.continue_with_email).click()
