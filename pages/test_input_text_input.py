from input_text_input import Input
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



def test_redirect_from_main_page(browser):
    browser.get ('https://www.qa-practice.com/elements/input/simple')
    browser.find_element(By.CLASS_NAME, 'has-sub').click()
    browser.find_element(By.CSS_SELECTOR, '.sub-menu[style*="display: block"]').click()
    browser.find_element(By.XPATH,'//a[@href="/elements/input"]').click()
    browser.find_element(By.ID, 'content').is_displayed()


def test_input_invalid_text(browser):
    input_page = Input(browser)
    input_page.open()
    input_page.text_input_tab().is_displayed()
    assert 'Text string*' == browser.find_element(By.CLASS_NAME, 'requiredField').text
    input_page.input_field().is_displayed()
    input_page.input_field().send_keys('.......')
    input_page.input_field().send_keys(Keys.RETURN)
    validation_message = browser.find_element(By.CLASS_NAME, 'invalid-feedback')
    validation_message.is_displayed()


def test_input_invalid_text(browser):
    input_page = Input(browser)
    input_page.open()
    input_page.text_input_tab().is_displayed()
    assert 'Text string*' == browser.find_element(By.CLASS_NAME, 'requiredField').text
    input_page.input_field().is_displayed()
    input_page.input_field().send_keys('Tets1')
    input_page.input_field().send_keys(Keys.RETURN)
    validation_message = browser.find_element(By.XPATH, '//p[1]')
    validation_message.is_displayed()
    input_page.input_field().is_displayed()
    input_page.input_field().send_keys(Keys.BACKSPACE)
    input_page.input_field().send_keys('T')
    input_page.input_field().send_keys(Keys.RETURN)
    validation_message = browser.find_element(By.XPATH, '//p[1]')
    validation_message.is_displayed()
    input_page.input_field().is_displayed()
    input_page.input_field().send_keys(Keys.BACKSPACE)
    input_page.input_field().send_keys('qweqweqweqweqweqweqweqweqweqweqwe')
    input_page.input_field().send_keys(Keys.RETURN)
    validation_message = browser.find_element(By.ID, 'error_1_id_text_string')
    validation_message.is_displayed()

def test_requirements_text(browser):
    input_page = Input(browser)
    input_page.open()
    requirements = input_page.browser.find_element(By.ID, 'req_header')
    requirements.is_displayed()
    requirements.click()
    browser.find_element(By.XPATH, '//li[contains(text(), "This is a required field")]').is_displayed()
    browser.find_element(By.XPATH, '//li[contains(text(), "User should be able to enter text into this field")]').is_displayed()
    browser.find_element(By.XPATH, '//li[contains(text(), "Text should be a valid string consisting of English letters, numbers, underscores or hyphens")]').is_displayed()
    browser.find_element(By.XPATH, '//li[contains(text(), "Text length limits:")]').is_displayed()
    browser.find_element(By.XPATH, '//li[contains(text(), "Max: 25 characters")]').is_displayed()
    browser.find_element(By.XPATH, '//li[contains(text(), "Min: 2 characters")]').is_displayed()
    browser.find_element(By.XPATH, '//li[contains(text(), "User can submit this one-field form by pressing Enter")]').is_displayed()
    browser.find_element(By.XPATH, '//li[contains(text(), "After submitting the form, the text entered by the user is displayed on the page")]').is_displayed()





