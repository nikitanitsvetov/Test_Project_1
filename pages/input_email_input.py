from time import sleep
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.remote.webelement import WebElement

class Input_email(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get(f'https://www.qa-practice.com/elements/input/email')
##

    def email_field(self) -> WebElement:
        return self.browser.find_element(By.XPATH, '//input[@class="textinput textInput form-control"]  ')

    def submit(self):
        self.email_field().send_keys(Keys.RETURN)

    def clear_input(self):
        self.email_field().clear()

    def is_validation_message_displayed(self):
        validation_message = self.browser.find_element(By.XPATH, '//span[@class="invalid-feedback"]')
        return validation_message.is_displayed()

    def input_flow(self, text: str, submit: bool = True) -> bool:
        self.clear_input()
        self.email_field().send_keys(text)
        sleep(1)
        if submit:
            self.submit()
        return self.is_validation_message_displayed()


    ##

    def requirements_text(self, text: str) -> WebElement:
        requirement_text = self.browser.find_element(By.XPATH, '//div[@class="collapse show"]//li[contains(text(),"'+text+'")]')
        return requirement_text