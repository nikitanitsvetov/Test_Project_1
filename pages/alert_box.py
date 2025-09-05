from base_page import BasePage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By



class AlertBox(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/alert/alert')

    def click_button(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "Click")]')

######################

    def alert_accept(self):
        self.browser.get('https://www.qa-practice.com/elements/alert/alert')
        alert_button = self.browser.find_element(By.XPATH, '//a[contains(text(), "Click")]')
        alert_button.click()
        alert = Alert(self.browser)
        alert.accept()

    def alert_dissmiss(self):
        self.browser.get('https://www.qa-practice.com/elements/alert/alert')
        alert_button = self.browser.find_element(By.XPATH, '//a[contains(text(), "Click")]')
        alert_button.click()
        alert = Alert(self.browser)
        alert.dismiss()


############

    def requirement(self):
        return self.browser.find_element(By.XPATH, '//a[@id="req_header"]')

    def requirements_text(self, text: str) -> WebElement:
        if '"' in text:
            xpath = f"//div[@class='collapse show']//li[contains(text(), '{text}')]"
        else:
            xpath = f'//div[@class="collapse show"]//li[contains(text(), "{text}")]'
        return self.browser.find_element(By.XPATH, xpath)
