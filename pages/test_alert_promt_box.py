from alert_promt_box import AlertPromtBox
import pytest
import allure

@allure.feature('Page elements')
def test_alert_box_check_page_elements(browser):
    alert_promt_box = AlertPromtBox(browser)
    alert_promt_box.open()
    alert_promt_box.click_button().is_displayed()
    alert_promt_box.requirement().is_displayed()

@allure.feature('Allert accept')
def test_allert_accept(browser):
    alert_promt_box = AlertPromtBox(browser)
    alert_promt_box.alert_accept()

@allure.feature('Allert dismiss')
def test_allert_dismiss(browser):
    alert_promt_box = AlertPromtBox(browser)
    alert_promt_box.alert_dissmiss()

def req_messages():
    return [
        'The page should have a Click button',
        'When the button is clicked, an alert is displayed to the user',
        'Alert window should display text "I am an alert!"',
        'The alert should have an OK, Cancel buttons and a text input field',
        'After clicking on the OK or Cancel button, the alert should be closed',
        "The user's input should be displayed on the page"
    ]
@allure.feature('Requirements verification')
@pytest.mark.parametrize('req_messages',req_messages())
def test_requirements(browser,req_messages):
    alert_promt_box = AlertPromtBox(browser)
    alert_promt_box.open()
    alert_promt_box.requirement().is_displayed()
    alert_promt_box.requirement().click()
    alert_promt_box.requirements_text(req_messages).is_displayed()