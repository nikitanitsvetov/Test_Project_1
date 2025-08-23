from main_page import Main
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



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

def test_ui_selector(browser):
    homepage = Main(browser)
    homepage.open()
    homepage.ui_elements().click()
    homepage.sub_menu().is_displayed()
    homepage.sub_menu_button('Inputs').is_displayed()
    homepage.sub_menu_button('Buttons').is_displayed()
    homepage.sub_menu_button('Checkbox').is_displayed()
    homepage.sub_menu_button('Select').is_displayed()
    homepage.sub_menu_button('New tab').is_displayed()
    homepage.sub_menu_button('Text area').is_displayed()
    homepage.sub_menu_button('Alerts').is_displayed()
    homepage.sub_menu_button('Drag and Drop').is_displayed()
    homepage.sub_menu_button('Iframes').is_displayed()
    homepage.sub_menu_button('Pop-Up').is_displayed()

def test_main_page_text(browser):
    homepage = Main(browser)
    homepage.open()
    homepage.browser.find_element(By.CSS_SELECTOR, 'h1').is_displayed()
    homepage.browser.find_element(By.CSS_SELECTOR, 'h1+p').is_displayed()
    homepage.browser.find_element(By.CSS_SELECTOR, 'h1+p+p').is_displayed()

def test_main_menu_visible(browser):
    homepage = Main(browser)
    homepage.open()
    homepage.main_menu_button('Text input').is_displayed()
    homepage.main_menu_button('Simple button').is_displayed()
    homepage.main_menu_button('Single checkbox').is_displayed()
    homepage.main_menu_button('Text area').is_displayed()
    homepage.main_menu_button('Select input').is_displayed()

def test_footer_visible(browser):
    homepage = Main(browser)
    homepage.open()
    homepage.contact_footer().is_displayed()
    homepage.what_new_footer().is_displayed()
    browser.find_element(By.CLASS_NAME, 'p-3').is_displayed()
    browser.find_element(By.XPATH, '//footer//a[@href="https://www.qa-practice.com/"]').is_displayed()













