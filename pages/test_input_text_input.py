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
    validation_message = browser.find_element(By.CLASS_NAME, 'invalid-feedback').is_displayed()






