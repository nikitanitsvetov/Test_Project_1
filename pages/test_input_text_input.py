from input_text_input import Input
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest



def test_redirect_from_main_page(browser):
    browser.get ('https://www.qa-practice.com/elements/input/simple')
    browser.find_element(By.CLASS_NAME, 'has-sub').click()
    browser.find_element(By.CSS_SELECTOR, '.sub-menu[style*="display: block"]').click()
    browser.find_element(By.XPATH,'//a[@href="/elements/input"]').click()
    browser.find_element(By.ID, 'content').is_displayed()

def test_input_valid_text(browser):
    input_page = Input(browser)
    input_page.open()
    input_page.text_input_tab().is_displayed()
    input_page.input_field().is_displayed()
    input_page.input_field().send_keys("Test")
    input_page.submit()
    validaton_window = browser.find_element(By.ID,'result')
    validaton_window.is_displayed()


def data():
    return ['T',' ','13123123123123123123123123123']
@pytest.mark.parametrize("user_data", data())
def test_input_invalid_text(browser, user_data):
    input_page = Input(browser)
    input_page.open()
    input_page.text_input_tab().is_displayed()
    assert 'Text string*' == browser.find_element(By.CLASS_NAME, 'requiredField').text
    input_page.input_flow(user_data)


def test_requirements_text(browser):
    input_page = Input(browser)
    input_page.open()
    requirements = input_page.browser.find_element(By.ID, 'req_header')
    requirements.is_displayed()
    requirements.click()
    input_page.requirements_text('This is a required field').is_displayed()
    input_page.requirements_text('User should be able to enter text into this field').is_displayed()
    ##input_page.requirements_text('Text length limits:').is_displayed()
    ##input_page.requirements_text('Max: 25 characters').is_displayed()
    ##input_page.requirements_text('Min: 2 characters').is_displayed()
    input_page.requirements_text('User can submit this one-field form by pressing Enter').is_displayed()
    input_page.requirements_text('After submitting the form, the text entered by the user is displayed on the page').is_displayed()








