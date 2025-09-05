from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

class DndBoxes(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/dragndrop/boxes')

###########

    def drag_element(self):
        return self.browser.find_element(By.XPATH, '//div[contains(text(), "Drag me")]')

    def drop_element(self):
        return self.browser.find_element(By.XPATH, '//p[contains(text(), "Drop here")]')

    def success_message(self):
        return self.browser.find_element(By.XPATH, '//p[contains(text(), "Dropped!")]')

    def drag_n_drop_func(self):
        actions = ActionChains(self.browser)
        actions.drag_and_drop(self.drag_element(), self.drop_element()).perform()

###########

    def requirement(self):
        return self.browser.find_element(By.XPATH, '//a[@id="req_header"]')

    def requirements_text(self, text: str) -> WebElement:
        if '"' in text:
            xpath = f"//div[@class='collapse show']//li[contains(text(), '{text}')]"
        else:
            xpath = f'//div[@class="collapse show"]//li[contains(text(), "{text}")]'
        return self.browser.find_element(By.XPATH, xpath)