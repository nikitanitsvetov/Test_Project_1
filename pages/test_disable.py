from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from disable import DisablePage


def test_dropdown_exist(browser):
    dropdown = DisablePage(browser)
    dropdown.open()
    assert dropdown.dropdown_is_displayed()

def test_dropdown_click(browser):
    dropdown = DisablePage(browser)
    dropdown.open()
    sorter = dropdown.dropdown()
    sorter.click()
    select = Select(sorter)
    select.select_by_value('enabled')
    dropdown.submit().click()
    assert 'Submitted' == dropdown.result_test()

def test_require_exist(browser):
    disable= DisablePage(browser)
    disable.open()
    assert disable.require()

def test_require_text1(browser):
    disable = DisablePage(browser)
    disable.open()
    disable.require_click()
    elm = disable.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[1]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'Submit button should be disabled by default.' == text

def test_require_text2(browser):
    disable = DisablePage(browser)
    disable.open()
    disable.require_click()
    elm = disable.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[2]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'User should be able to enable and then disable the button using the options of the Select state dropdown.' == text

def test_require_text3(browser):
    disable = DisablePage(browser)
    disable.open()
    disable.require_click()
    elm = disable.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[3]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'The option selected in the dropdown should be applied to the button immediately.' == text

def test_require_text4(browser):
    disable = DisablePage(browser)
    disable.open()
    disable.require_click()
    elm = disable.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[4]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'After pressing the button, the user should be shown confirmation that the button was pressed.' == text