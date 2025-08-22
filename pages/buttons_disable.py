from base_page import BasePage
from selenium.webdriver.common.by import By
import pytest


dropdown_selector = (By.ID, 'id_select_state')
button_submit = (By.ID, 'submit-id-submit')
result = (By.ID, 'result-text')
require = (By.ID, 'req_header')


class DisablePage(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(f'https://www.qa-practice.com/elements/button/disabled')

    def dropdown(self):
        return self.find(dropdown_selector)

    def dropdown_is_displayed(self):
        return self.dropdown().is_displayed()

    def click_dropdown(self):
        self.dropdown().click()



    def submit(self):
        return self.find(button_submit)

    def submit_is_disp(self):
        return self.submit().is_displayed()



    def result(self):
        return self.find(result)

    def result_test(self):
        return self.result().text



    def require(self):
        return self.find(require)

    def require_click(self):
        self.require().click()

