from selenium.webdriver.common.by import By
from look_like_button import LookLikeButton
import pytest


def test_button2_exist(browser):
    look_like_button =  LookLikeButton(browser)
    look_like_button.open()
    assert look_like_button.button_is_displayed()

def test_button2_clicked(browser):
    looks_like_button = LookLikeButton(browser)
    looks_like_button.open()
    looks_like_button.button().click()
    assert 'Submitted' == looks_like_button.result_test()

def test_require_exist(browser):
    look_like_button = LookLikeButton(browser)
    look_like_button.open()
    assert look_like_button.require()

def test_require_clicked(browser):
    look_like_button = LookLikeButton(browser)
    look_like_button.open()
    look_like_button.require_click()

def test_require_text1(browser):
    look_like_button = LookLikeButton(browser)
    look_like_button.open()
    look_like_button.require_click()
    elm = look_like_button.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[1]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'The user should be able to click the button.' == text

def test_require_text2(browser):
    look_like_button = LookLikeButton(browser)
    look_like_button.open()
    look_like_button.require_click()
    elm = look_like_button.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[2]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'The button should be labeled Click.' == text

def test_require_text3(browser):
    simple_page = LookLikeButton(browser)
    simple_page.open()
    simple_page.require_click()
    elm = simple_page.browser.find_element(By.XPATH, '//div[@class = "card card-body"]//li[3]')
    text = browser.execute_script("return arguments[0].textContent;", elm)
    assert 'After pressing the button, the user should be shown confirmation that the button was pressed.' == text


    ##print(looks_like_button.subMenuButton('Checkbox').is_displayed())
    ##print(looks_like_button.subMenuButton('Buttons').is_displayed())