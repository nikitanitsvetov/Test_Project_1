
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class Checkboxes(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get(f'https://www.qa-practice.com/elements/checkbox/mult_checkbox')


    def labels(self):
        return self.browser.find_element(By.XPATH, '//label[contains(text(),"Checkboxes")]')

    def checkbox(self, text: str) ->WebElement:
        return self.browser.find_element(By.XPATH, '//label[contains(text(), "' +text+ '")]/../input[@type="checkbox"]')

    def submit(self):
        return self.browser.find_element(By.XPATH, '//input[@id="submit-id-submit"]')

    def submit_message(self):
        return self.browser.find_element(By.XPATH, '//div/p[1]')

    def requirement(self):
        return self.browser.find_element(By.XPATH, '//a[@id="req_header"]')

    def requirements_text(self, text: str) -> WebElement:
        requirement_text = self.browser.find_element(By.XPATH,
                                                     '//div[@class="collapse show"]//li[contains(text(),'
                                                     '"' + text + '")]')
        return requirement_text

