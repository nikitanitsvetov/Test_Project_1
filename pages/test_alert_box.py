from alert_box import AlertBox
import pytest
import allure

@allure.feature('Page elements')
def test_alert_box_check_page_elements(browser):
    alert_box = AlertBox(browser)
    alert_box.open()
    alert_box.click_button().is_displayed()
    alert_box.requirement().is_displayed()

@allure.feature('Allert accept')
def test_allert_accept(browser):
    alert_box = AlertBox(browser)
    alert_box.alert_accept()

def req_messages():
    return [
        'The page should have a Click button',
        'When the button is clicked, an alert is displayed to the user',
        'Alert window should display text "I am an alert!"',
        'The alert should have an OK button',
        'After clicking on the OK button, the alert should be closed'
    ]
@allure.feature('Requirements verification')
@pytest.mark.parametrize('req_messages',req_messages())
def test_requirements(browser,req_messages):
    alert_box = AlertBox(browser)
    alert_box.open()
    alert_box.requirement().is_displayed()
    alert_box.requirement().click()
    alert_box.requirements_text(req_messages).is_displayed()