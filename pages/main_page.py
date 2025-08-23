from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import pytest




UI_selector = (By.CLASS_NAME, 'has-sub')
sub_menu = (By.CSS_SELECTOR, '.sub-menu[style*="display: block"]')
Contact = (By.XPATH, '//a[text()="Contact"]')
what_new = (By.XPATH, '//a[@href="/whats_new/"]')



class Main(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(f'https://www.qa-practice.com/')

    def ui_elements(self):
        return self.find(UI_selector)

    def sub_menu(self):
        return self.find(sub_menu)

    def sub_menu_button(self, text: str) -> WebElement:
        return self.browser.find_element(By.XPATH, '//ul[@class="sub-menu"]//a[text()="'+text+'"]')

    def main_menu_button(self, text: str) -> WebElement:
        return self.browser.find_element(By.XPATH, '//ol[@class="rectangle"]//a[text()="'+text+'"]')

    def contact_footer(self):
        return self.find(Contact)
    def what_new_footer(self):
        return self.find(what_new)

