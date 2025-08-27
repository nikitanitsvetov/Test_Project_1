from selenium.webdriver.common.by import By
import pytest
from input_password_input import Input_password




def test_email_page_is_visible(browser):
    email_page = Input_password(browser)
    email_page.open()
    email_page.password_field().is_displayed()

def data():
    return [
        '12345',
        'test',
        'Test',
        'Test1'
    ]
@pytest.mark.parametrize("user_data", data())
def test_email_validation(browser, user_data):
    email_page = Input_password(browser)
    email_page.open()
    browser.find_element(By.XPATH, '//label[@class="form-label requiredField"]').is_displayed()
    email_page.input_flow(user_data)

def test_valid_password(browser):
    input_page = Input_password(browser)
    input_page.open()
    input_page.password_field().is_displayed()
    input_page.password_field().send_keys('Passworder12!')
    input_page.password_field().submit()
    input_page.sucsess().is_displayed()

def datas():
    return [
        'Has minimum 8 characters in length',
        'At least one uppercase English letter',
        'At least one lowercase English letter',
        'At least one digit',
        'At least one special character',
        'User can submit this one-field form by pressing Enter',
        'After submitting the form, the text entered by the user is displayed on the page'
    ]
@pytest.mark.parametrize("datas", datas())

def test_requirements_text(browser, datas):
    input_page = Input_password(browser)
    input_page.open()
    requirements = input_page.browser.find_element(By.ID, 'req_header')
    requirements.is_displayed()
    requirements.click()
    input_page.requirements_text(datas)

