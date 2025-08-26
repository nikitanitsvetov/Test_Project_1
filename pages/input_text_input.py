from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.remote.webelement import WebElement

from pages.conftest import browser

text_input_tab = (By.XPATH, '//a[@href="/elements/input/simple"]')
requirements = (By.ID, 'req_header')


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
        return self.browser.find_element(By.XPATH, '//*[@placeholder = "Submit me"] ')

    def clear_input(self):
        self.input_field().clear()

    def submit(self):
        self.input_field().send_keys(Keys.RETURN)

    def is_validation_message_displayed(self):
        validation_message = self.browser.find_element(By.ID, 'error_1_id_text_string')
        return validation_message.is_displayed()

    def requirements_text(self, text: str) -> WebElement:
        return self.browser.find_element(By.XPATH, '//div[@class="collapse show"]//li[text()="'+text+'"]')

    def input_flow(self, text: str, submit: bool = True) -> bool:
        """Полный flow: очистка, ввод, отправка, проверка валидации"""
        self.clear_input()
        self.input_field().send_keys(text)
        if submit:
            self.submit()
        return self.is_validation_message_displayed()


