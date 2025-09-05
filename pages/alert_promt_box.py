from base_page import BasePage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By



class AlertPromtBox(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/alert/prompt#')

    def click_button(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "Click")]')

######################

    def alert_accept(self):
        self.browser.get('https://www.qa-practice.com/elements/alert/prompt#')
        alert_button = self.browser.find_element(By.XPATH, '//a[contains(text(), "Click")]')
        alert_button.click()
        alert = Alert(self.browser)
        input_text = 'one'
        alert.send_keys(input_text)
        alert.accept()
        sucsess_message = self.browser.find_element(By.XPATH, '//p[@id="result-text"]')
        sucsess_message.is_displayed()

    def alert_dissmiss(self):
        self.browser.get('https://www.qa-practice.com/elements/alert/prompt#')
        alert_button = self.browser.find_element(By.XPATH, '//a[contains(text(), "Click")]')
        alert_button.click()
        alert = Alert(self.browser)
        alert.dismiss()
        sucsess_message = self.browser.find_element(By.XPATH, '//p[contains(text(), "You canceled the prompt")]')
        sucsess_message.is_displayed()



############

    def requirement(self):
        return self.browser.find_element(By.XPATH, '//a[@id="req_header"]')

    def requirements_text(self, text: str) -> WebElement:
        if '"' in text:
            xpath = f"//div[@class='collapse show']//li[contains(text(), '{text}')]"
        else:
            xpath = f'//div[@class="collapse show"]//li[contains(text(), "{text}")]'
        return self.browser.find_element(By.XPATH, xpath)
