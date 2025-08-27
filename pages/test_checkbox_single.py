from selenium.webdriver.common.by import By
import pytest
from checkbox_single import Checkbox_single
from selenium import webdriver


def test_checkbox_presented(browser):
    checkbox = Checkbox_single(browser)
    checkbox.open()
    checkbox.checkbox().is_displayed()
    label = browser.find_element(By.XPATH, '//div//label[contains(text(), "Checkbox")]')
    label.is_displayed()
    label2 = browser.find_element(By.XPATH, '//div//label[contains(text(), "Select")]')
    label2.is_displayed()
    checkbox.submit_button().is_displayed()


def test_checkbox_happypass(browser):
    checkbox = Checkbox_single(browser)
    checkbox.open()
    checkbox.checkbox().is_displayed()
    checkbox.checkbox().click()
    checkbox.submit_button().is_displayed()
    checkbox.submit_button().click()
    happy_message = browser.find_element(By.XPATH, '//div//p[@class]')
    happy_message.is_displayed()

def datas():
    return [
        'There should be one checkbox on the page.',
        'The label of the checkbox should be',
        'The user should be able to select the checkbox',
        'The Submit button should always be enabled',
        'After submitting the user should get the following result:',
        'if the checkbox was not selected, then the result is not displayed',
        'if a checkbox has been selected, the name of the selected checkbox is displayed to the user'
    ]

@pytest.mark.parametrize("datas", datas())
def test_requirements_text(browser, datas):
    input_page = Checkbox_single(browser)
    input_page.open()
    requirements = input_page.browser.find_element(By.ID, 'req_header')
    requirements.is_displayed()
    requirements.click()
    input_page.requirements_text(datas)
