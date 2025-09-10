from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import allure


UI_selector = (By.CLASS_NAME, 'has-sub')
sub_menu = (By.CSS_SELECTOR, '.sub-menu[style*="display: block"]')
Contact = (By.XPATH, '//a[text()="Contact"]')
what_new = (By.XPATH, '//a[@href="/whats_new/"]')
requirements = (By.ID, 'req_header')


class Main(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open Browser'):
            self.browser.get(f'https://www.qa-practice.com/')

########

    def ui_elements(self):
        with allure.step('page text verification'):
            return self.find(UI_selector)

    def logo_image(self):
        return self.browser.find_element(By.XPATH, '//img[@class = "logo_image"]')

    def button_poicture(self):
        return self.browser.find_element(By.XPATH, '//i[@class="fa fa-th-large"]  ')


    def sub_menu(self):
        with allure.step('Sub menu verification'):
            return self.find(sub_menu)

    def sub_menu_button(self, text: str) -> WebElement:
        with allure.step('All sub menus list verivication'):
            return self.browser.find_element(By.XPATH, '//ul[@class="sub-menu"]//a[text()="'+text+'"]')

    def main_menu_button(self, text: str) -> WebElement:
        with allure.step('mein menu button verivication'):
            return self.browser.find_element(By.XPATH, '//ol[@class="rectangle"]//a[text()="'+text+'"]')

########

    def contact_footer(self):
        with allure.step('First footer verification'):
            return self.find(Contact)

    def what_new_footer(self):
        with allure.step('Second footer verification'):
            return self.find(what_new)

