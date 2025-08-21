from selenium.webdriver.common.by import By
from simple_button import SimpleButtonPage


def test_button1_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()

def test_button1_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.click_button()
    assert 'Submitted' == simple_page.result_test()

def test_require_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.require()

def test_require_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.require_click()

def test_require_text1(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.require_click()
    elm = simple_page.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[1]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'The user should be able to click the button.' == text

def test_require_text2(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.require_click()
    elm = simple_page.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[2]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'The button should be labeled Click.' == text

def test_require_text3(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.require_click()
    elm = simple_page.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[3]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'After pressing the button, the user should be shown confirmation that the button was pressed.' == text