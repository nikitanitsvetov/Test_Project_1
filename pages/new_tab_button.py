from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement

from pages.conftest import browser


class NewTabButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/new_tab/button')

    def button(self):
        return self.browser.find_element(By.XPATH, '//a[@class="a-button"]')

    def get_page_url(self):
        return self.browser.current_url

    def new_page(self):
        original_tab = self.browser.current_window_handle
        new_tab = [tab for tab in self.browser.window_handles if tab != original_tab][0]
        self.browser.switch_to.window(new_tab)
        return self

########

    def sucsess_message(self):
        return self.browser.find_element(By.XPATH, '//p[@class = "result-text"]')

########


    def requirement(self):
        return self.browser.find_element(By.XPATH, '//a[@id="req_header"]')



    def requirements_text(self, text: str) -> WebElement:
        if '"' in text:
            xpath = f"//div[@class='collapse show']//li[contains(text(), '{text}')]"
        else:
            xpath = f'//div[@class="collapse show"]//li[contains(text(), "{text}")]'
        return self.browser.find_element(By.XPATH, xpath)

