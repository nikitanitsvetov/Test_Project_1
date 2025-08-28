from selenium.webdriver.common.by import By
from buttons_simple_button import SimpleButtonPage
import allure

@allure.feature('Button_simple_button')
def test_button1_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()

@allure.feature('Button_simple_button')
def test_button1_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.click_button()
    assert 'Submitted' == simple_page.result_test()

@allure.feature('Button_simple_button')
def test_require_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.require()

@allure.feature('Button_simple_button')
def test_require_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.require_click()

@allure.feature('Button_simple_button')
def test_require_text1(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.require_click()
    elm = simple_page.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[1]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'The user should be able to click the button.' == text

@allure.feature('Button_simple_button')
def test_require_text2(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.require_click()
    elm = simple_page.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[2]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'The button should be labeled Click.' == text

@allure.feature('Button_simple_button')
def test_require_text3(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.require_click()
    elm = simple_page.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[3]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'After pressing the button, the user should be shown confirmation that the button was pressed.' == text

