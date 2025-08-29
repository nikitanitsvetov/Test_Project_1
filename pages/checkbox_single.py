
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class Checkbox_single(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get(f'https://www.qa-practice.com/elements/checkbox/single_checkbox')
##
    def checkbox(self)-> WebElement:
        return self.browser.find_element(By.XPATH, '//input[@class="form-check-input"]')

    def submit_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]')

##
    def requirements_text(self, text: str) -> WebElement:
        if '"' in text:
            xpath = f"//div[@class='collapse show']//li[contains(text(), '{text}')]"
        else:
            xpath = f'//div[@class="collapse show"]//li[contains(text(), "{text}")]'
        return self.browser.find_element(By.XPATH, xpath)