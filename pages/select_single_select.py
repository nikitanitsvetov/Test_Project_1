from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement




class SelectSingleSelect(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/select/single_select')

    def title(self):
        return self.browser.find_element(By.XPATH, '//label[@class="form-label requiredField"]')



    def dropdown(self):
        return self.browser.find_element(By.XPATH, '//select[@class="form-select"]')

    def dropdown_select_value(self, value):
        dropdown = self.dropdown()
        select = Select(dropdown)
        select.select_by_value(value)
        return self

    def get_selected_value(self):
        dropdown = self.dropdown()
        select = Select(dropdown)
        return select.first_selected_option.get_attribute("value")

    def get_selected_text(self):
        dropdown = self.dropdown()
        select = Select(dropdown)
        return select.first_selected_option.text

    def should_have_selected_value(self, expected_value):
        actual_value = self.get_selected_value()
        assert actual_value == expected_value, f"Expected value: {expected_value}, but got: {actual_value}"
        return self

    def should_have_selected_text(self, expected_text):
        actual_text = self.get_selected_text()
        assert actual_text == expected_text, f"Expected text: {expected_text}, but got: {actual_text}"
        return self


    def submit(self):
        return self.browser.find_element(By.XPATH, '//input[@id="submit-id-submit"]')

    def requirement(self):
        return self.browser.find_element(By.XPATH, '//a[@id="req_header"]')

    def requirements_text(self, text: str) -> WebElement:
        if '"' in text:
            xpath = f"//div[@class='collapse show']//li[contains(text(), '{text}')]"
        else:
            xpath = f'//div[@class="collapse show"]//li[contains(text(), "{text}")]'
        return self.browser.find_element(By.XPATH, xpath)

