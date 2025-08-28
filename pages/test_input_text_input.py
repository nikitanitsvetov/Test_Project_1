from input_text_input import Input
from selenium.webdriver.common.by import By
import pytest
import allure


@allure.feature('Input_text')
def test_redirect_from_main_page(browser):
    browser.get ('https://www.qa-practice.com/elements/input/simple')
    browser.find_element(By.CLASS_NAME, 'has-sub').click()
    browser.find_element(By.CSS_SELECTOR, '.sub-menu[style*="display: block"]').click()
    browser.find_element(By.XPATH,'//a[@href="/elements/input"]').click()
    browser.find_element(By.ID, 'content').is_displayed()

@allure.feature('Input_text')
def test_input_valid_text(browser):
    input_page = Input(browser)
    input_page.open()
    input_page.text_input_tab().is_displayed()
    input_page.input_field().is_displayed()
    input_page.input_field().send_keys("Test")
    input_page.submit()
    validaton_window = browser.find_element(By.ID,'result')
    assert validaton_window.is_displayed()

def data():
    return ['T',' ','13123123123123123123123123123']
@allure.feature('Input_text')
@pytest.mark.parametrize("user_data", data())
def test_input_invalid_text(browser, user_data):
    input_page = Input(browser)
    input_page.open()
    input_page.text_input_tab().is_displayed()
    assert 'Text string*' == browser.find_element(By.CLASS_NAME, 'requiredField').text
    input_page.input_flow(user_data)

def datas():
    return [
        'This is a required field',
        'User should be able to enter text into this field',
        'Text length limits:',
        'Max: 25 characters',
        'Min: 2 characters',
        'User can submit this one-field form by pressing Enter',
        'After submitting the form, the text entered by the user is displayed on the page'
    ]
@allure.feature('Input_text')
@pytest.mark.parametrize("data", datas())
def test_requirements_text(browser, data):
    input_page = Input(browser)
    input_page.open()
    requirements = input_page.browser.find_element(By.ID, 'req_header')
    requirements.is_displayed()
    requirements.click()
    assert input_page.requirements_text(data).is_displayed()





