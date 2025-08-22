from base_page import BasePage
from selenium.webdriver.common.by import By
import pytest



button_selector = (By.ID, 'submit-id-submit')
button_result = (By.ID, 'result-text')
require = (By.ID, 'req_header')


class SimpleButtonPage(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(f'https://www.qa-practice.com/elements/button/simple')

    def click_button(self):
        self.button().click()

    def button(self):
        return self.find(button_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def result(self):
        return self.find(button_result)

    def result_test(self):
        return self.result().text

    def require(self):
        return self.find(require)

    def require_click(self):
        self.require().click()

