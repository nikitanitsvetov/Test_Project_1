from textarea_textarea import TextArea
import pytest
import allure

def test_page_elemets(browser):
    page_element = TextArea(browser)
    page_element.open()
    page_element.text_input_field().is_displayed()
    page_element.field_text_ares().is_displayed()
    page_element.submit_button().is_displayed()
    page_element.requirement().is_displayed()

def test_input_text(browser):
    page_element = TextArea(browser)
    page_element.open()
    page_element.text_input_field().send_keys('12344123')
    page_element.submit_button().click()
    page_element.sucses().is_displayed()

def req_messages():
    return [
        'Field name is "Text area"',
        'This is a required field',
        'User should be able to enter any text into this field',
        'The result can be sent using the Submit button',
        'After submitting the form, the text entered by the user is displayed on the page'
    ]
@allure.feature('Requirements verification')
@pytest.mark.parametrize('req_messages',req_messages())
def test_requirements(browser,req_messages):
    page_element = TextArea(browser)
    page_element.open()
    page_element.requirement().is_displayed()
    page_element.requirement().click()
    page_element.requirements_text(req_messages).is_displayed()