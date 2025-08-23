from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import pytest

text_input_tab = (By.XPATH, '//a[@href="/elements/input/simple"]')
input_field = (By.CLASS_NAME, 'form-control')


class Input(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get(f'https://www.qa-practice.com/elements/input')


    def sub_menu_button(self, text: str) -> WebElement:
        return self.browser.find_element(By.XPATH, '//ul[@class="sub-menu"]//a[text()="'+text+'"]')

    def text_input_tab(self):
        return self.find(text_input_tab)

    def input_field(self):
        return self.find(input_field)

