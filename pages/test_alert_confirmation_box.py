from alert_confirmation_box import AlertConfirmationBox
import pytest
import allure

@allure.feature('Page elements')
def test_alert_box_check_page_elements(browser):
    alert_confirmation_box = AlertConfirmationBox(browser)
    alert_confirmation_box.open()
    alert_confirmation_box.click_button().is_displayed()
    alert_confirmation_box.requirement().is_displayed()

@allure.feature('Allert accept')
def test_allert_accept(browser):
    alert_confirmation_box = AlertConfirmationBox(browser)
    alert_confirmation_box.alert_accept()

@allure.feature('Allert dismiss')
def test_allert_dismiss(browser):
    alert_confirmation_box = AlertConfirmationBox(browser)
    alert_confirmation_box.alert_dissmiss()

def req_messages():
    return [
        'The page should have a Click button',
        'When the button is clicked, an alert is displayed to the user',
        'Alert window should display text "I am an alert!"',
        'The alert should have an OK and Cancel buttons',
        'After clicking on the OK or Cancel button, the alert should be closed',
        "The user's choice should be displayed on the page"
    ]
@allure.feature('Requirements verification')
@pytest.mark.parametrize('req_messages',req_messages())
def test_requirements(browser,req_messages):
    alert_confirmation_box = AlertConfirmationBox(browser)
    alert_confirmation_box.open()
    alert_confirmation_box.requirement().is_displayed()
    alert_confirmation_box.requirement().click()
    alert_confirmation_box.requirements_text(req_messages).is_displayed()