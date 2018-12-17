from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.views.locators import Locators


class BasePage(object):
    def __init__ (self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(driver, 10)
        self.timeout = 500

    def wait_until_progress_bar_disappear(self):
        self.wait.until_not(EC.visibility_of_element_located(Locators.progress_bar))

    def wait_until_element_appear(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def change_current_view(self):
        self.wait_until_element_appear(Locators.change_current_view).click()

    def refresh_view(self):
        height, weight = self.driver.get_window_size()['height'], \
                         self.driver.get_window_size()['width']
        start_x = weight / 2.1
        end_y= height * 0.8
        start_y = height * 0.21
        self.driver.swipe(start_x , start_y, start_x, end_y, 2000)
