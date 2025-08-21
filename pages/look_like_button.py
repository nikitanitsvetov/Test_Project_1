from selenium.webdriver.remote.webelement import WebElement
from base_page import BasePage
from selenium.webdriver.common.by import By
import pytest



button_selector = (By.XPATH, '//a[text()="Click"]')
button_result = (By.ID,'result-text')
require = (By.ID, 'req_header')

class LookLikeButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(f'https://www.qa-practice.com/elements/button/like_a_button')

    def click_button(self):
        self.button().click()

    def button(self):
        return self.find(button_selector)

    def sub_menu_button(self, text: str) -> WebElement:
        return self.browser.find_element(By.XPATH, '//ul[@class="sub-menu"]//a[text()="'+text+'"]')

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