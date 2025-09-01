from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import random



class MultipleSelect(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/select/mult_select')

    def page_text(self, text: str)->WebElement:
        return self.browser.find_element(By.XPATH, f'//*[contains(text(), "{text}")]')

######################

    def dropdown1(self):
        return self.browser.find_element(By.XPATH, '//select[@id = "id_choose_the_place_you_want_to_go"]')

    def dropdown_select_value1(self, value):
        dropdown = self.dropdown1()
        select = Select(dropdown)
        select.select_by_value(value)
        return self

    def dropdown_select_random_value1(self):
        dropdown = self.dropdown1()
        select = Select(dropdown)
        values = []
        for option in select.options:
            value = option.get_attribute("value")
            if value and value.strip():
                values.append(value)
        random_value = random.choice(values)
        select.select_by_value(random_value)
        return random_value

    def get_selected_value1(self):
        dropdown = self.dropdown1()
        select = Select(dropdown)
        return select.first_selected_option.get_attribute("value")

    def get_selected_text1(self):
        dropdown = self.dropdown1()
        select = Select(dropdown)
        return select.first_selected_option.text

    def should_have_selected_value1(self, expected_value):
        actual_value = self.get_selected_value1()
        assert actual_value == expected_value, f"Expected value: {expected_value}, but got: {actual_value}"
        return self

    def should_have_selected_text1(self, expected_text):
        actual_text = self.get_selected_text1()
        assert actual_text == expected_text, f"Expected text: {expected_text}, but got: {actual_text}"
        return self

######################

    def dropdown2(self):
        return self.browser.find_element(By.XPATH, '//select[@id = "id_choose_how_you_want_to_get_there"]')

    def dropdown_select_value2(self, value):
        dropdown = self.dropdown2()
        select = Select(dropdown)
        select.select_by_value(value)
        return self

    def dropdown_select_random_value2(self):
        dropdown = self.dropdown2()
        select = Select(dropdown)
        values = []
        for option in select.options:
            value = option.get_attribute("value")
            if value and value.strip():
                values.append(value)
        random_value = random.choice(values)
        select.select_by_value(random_value)
        return random_value

    def get_selected_value2(self):
        dropdown = self.dropdown2()
        select = Select(dropdown)
        return select.first_selected_option.get_attribute("value")

    def get_selected_text2(self):
        dropdown = self.dropdown2()
        select = Select(dropdown)
        return select.first_selected_option.text

    def should_have_selected_value2(self, expected_value):
        actual_value = self.get_selected_value2()
        assert actual_value == expected_value, f"Expected value: {expected_value}, but got: {actual_value}"
        return self

    def should_have_selected_text2(self, expected_text):
        actual_text = self.get_selected_text2()
        assert actual_text == expected_text, f"Expected text: {expected_text}, but got: {actual_text}"
        return self

######################

    def dropdown3(self):
        return self.browser.find_element(By.XPATH, '//select[@id = "id_choose_when_you_want_to_go"]')

    def dropdown_select_value3(self, value):
        dropdown = self.dropdown3()
        select = Select(dropdown)
        select.select_by_value(value)
        return self

    def dropdown_select_random_value3(self):
        dropdown = self.dropdown3()
        select = Select(dropdown)
        values = []
        for option in select.options:
            value = option.get_attribute("value")
            if value and value.strip():
                values.append(value)
        random_value = random.choice(values)
        select.select_by_value(random_value)
        return random_value




    def get_selected_value3(self):
        dropdown = self.dropdown3()
        select = Select(dropdown)
        return select.first_selected_option.get_attribute("value")

    def get_selected_text3(self):
        dropdown = self.dropdown3()
        select = Select(dropdown)
        return select.first_selected_option.text

    def should_have_selected_value3(self, expected_value):
        actual_value = self.get_selected_value3()
        assert actual_value == expected_value, f"Expected value: {expected_value}, but got: {actual_value}"
        return self

    def should_have_selected_text3(self, expected_text):
        actual_text = self.get_selected_text3()
        assert actual_text == expected_text, f"Expected text: {expected_text}, but got: {actual_text}"
        return self

######################

    def submit(self):
        return self.browser.find_element(By.XPATH, '//input[@id="submit-id-submit"]')

    def submit_message(self):
        return self.browser.find_element(By.XPATH, '//div[@class="result"]')

    def requirement(self):
        return self.browser.find_element(By.XPATH, '//a[@id="req_header"]')

    def requirements_text(self, text: str) -> WebElement:
        if '"' in text:
            xpath = f"//div[@class='collapse show']//li[contains(text(), '{text}')]"
        else:
            xpath = f'//div[@class="collapse show"]//li[contains(text(), "{text}")]'
        return self.browser.find_element(By.XPATH, xpath)

