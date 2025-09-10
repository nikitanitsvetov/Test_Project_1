from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement



class TextArea(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/textarea/single')

    ##########

    def field_text_ares(self):
        return  self.browser.find_element(By.XPATH, '//label[@class="form-label requiredField"]')

    def text_input_field(self):
        return self.browser.find_element(By.XPATH, '//textarea[@name="text_area"]')

    def submit_button(self):
        return self.browser.find_element(By.XPATH,'//input[@type="submit"]')

    def sucses(self):
        return self.browser.find_element(By.XPATH, '//div[@class="result"]')

    ##########

    def requirement(self):
        return self.browser.find_element(By.XPATH, '//a[@id="req_header"]')

    def requirements_text(self, text: str) -> WebElement:
        if '"' in text:
            xpath = f"//div[@class='collapse show']//li[contains(text(), '{text}')]"
        else:
            xpath = f'//div[@class="collapse show"]//li[contains(text(), "{text}")]'
        return self.browser.find_element(By.XPATH, xpath)

