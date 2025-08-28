from selenium.webdriver.common.by import By
import pytest
from input_email_input import Input_email
import allure


@allure.feature('Input_email')
def test_email_page_is_visible(browser):
    email_page = Input_email(browser)
    email_page.open()
    assert  email_page.email_field().is_displayed()

def data():
    return ['1234','nike.gmail.com',' ']
@allure.feature('Input_email')
@pytest.mark.parametrize("user_data", data())
def test_email_validation(browser, user_data):
    email_page = Input_email(browser)
    email_page.open()
    browser.find_element(By.XPATH, '//label[@class="form-label requiredField"]').is_displayed()
    email_page.input_flow(user_data)

@allure.feature('Input_email')
def test_valid_message(browser):
    input_page = Input_email(browser)
    input_page.open()
    input_page.email_field().is_displayed()
    input_page.email_field().send_keys('test@mail.ru')
    input_page.email_field().submit()
    assert input_page.sucsess().is_displayed()

def datas():
    return [
        'Entered text should be a valid email address',
        'domain should be allowed',
        'User can submit this one-field form by pressing Enter',
        'After submitting the form, the text entered by the user is displayed on the page'
    ]
@allure.feature('Input_email')
@pytest.mark.parametrize("datas", datas())
def test_requirements_text(browser, datas):
    input_page = Input_email(browser)
    input_page.open()
    requirements = input_page.browser.find_element(By.ID, 'req_header')
    requirements.is_displayed()
    requirements.click()
    assert input_page.requirements_text(datas).is_displayed()

