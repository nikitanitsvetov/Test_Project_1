from main_page import Main
from selenium.webdriver.common.by import By
import pytest



def test_logo_is_visible(browser):
    main = Main(browser)
    main.open()
    logo = main.browser.find_element(By.CLASS_NAME,'logo_image')
    logo.is_displayed()

def test_home_page_button_is_displayed(browser):
    homepage = Main(browser)
    homepage.open()
    logo = homepage.browser.find_element(By.CLASS_NAME, 'fa-th-large')
    logo.is_displayed()

def data1():
    return [
        'Inputs',
        'Buttons',
        'Checkbox',
        'Select',
        'New tab',
        'Text area',
        'Alerts',
        'Drag and Drop',
        'Iframes',
        'Pop-Up'
    ]
@pytest.mark.parametrize("data1", data1())
def test_ui_selector(browser, data1):
    homepage = Main(browser)
    homepage.open()
    homepage.ui_elements().click()
    homepage.sub_menu().is_displayed()
    homepage.sub_menu_button(data1).is_displayed()

def test_main_page_text(browser):
    homepage = Main(browser)
    homepage.open()
    homepage.browser.find_element(By.CSS_SELECTOR, 'h1').is_displayed()
    homepage.browser.find_element(By.CSS_SELECTOR, 'h1+p').is_displayed()
    homepage.browser.find_element(By.CSS_SELECTOR, 'h1+p+p').is_displayed()


def data2():
    return [
        'Text input',
        'Simple button',
        'Single checkbox',
        'Text area',
        'Select input',
    ]
@pytest.mark.parametrize("data2", data2())
def test_main_menu_visible(browser, data2):
    homepage = Main(browser)
    homepage.open()
    homepage.main_menu_button(data2).is_displayed()

def test_footer_visible(browser):
    homepage = Main(browser)
    homepage.open()
    homepage.contact_footer().is_displayed()
    homepage.what_new_footer().is_displayed()
    browser.find_element(By.CLASS_NAME, 'p-3').is_displayed()
    browser.find_element(By.XPATH, '//footer//a[@href="https://www.qa-practice.com/"]').is_displayed()













