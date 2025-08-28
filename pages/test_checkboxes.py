import pytest
from checkboxes import Checkboxes
import allure




def data():
    return [
        'One',
        'Two',
        'Three'
    ]
@allure.feature('Checkboxes')
@pytest.mark.parametrize("data", data())
def test_checkboxes_page_visible(browser, data):
    checkboxes_page = Checkboxes(browser)
    checkboxes_page.open()
    checkboxes_page.labels().is_displayed()
    checkboxes_page.checkbox(data).is_displayed()
    checkboxes_page.submit().is_displayed()
    assert checkboxes_page.requirement().is_displayed()

@allure.feature('Checkboxes')
def test_check_checkboxes(browser):
    checkboxes_page = Checkboxes(browser)
    checkboxes_page.open()
    specific_checkboxes1 = [data()[0]]
    for checkbox_name in specific_checkboxes1:
        checkboxes_page.checkbox(checkbox_name).click()
    browser.refresh()
    specific_checkboxes2 = data()[:2]
    for checkbox_name in specific_checkboxes2:
        checkboxes_page.checkbox(checkbox_name).click()
    checkboxes_page.submit().click()
    assert checkboxes_page.submit_message().is_displayed()

def datas():
    return [
        'There should be three checkboxes on the page.',
        'The label of the checkboxes should be:',
        'One',
        'Two',
        'Three',
        'The user should be able to select any checkbox',
        'The Submit button should always be enabled',
        'After submitting the user should get the following result:',
        'if no checkbox was selected, then the result is not displayed',
        'if a checkbox has been selected, the name(s) of the selected checkbox(es) is(are) displayed to the user'
    ]
@allure.feature('Checkboxes')
@pytest.mark.parametrize("datas", datas())
def test_requirement_text(browser, datas):
    checkboxes_page = Checkboxes(browser)
    checkboxes_page.open()
    checkboxes_page.requirement().click()
    assert checkboxes_page.requirements_text(datas).is_displayed()


