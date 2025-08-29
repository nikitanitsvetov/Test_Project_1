from select_single_select import SelectSingleSelect
import pytest
import allure

@allure.feature('Select_single_dropdown')
def test_select_single_select_page_vivble(browser):
    single_select = SelectSingleSelect(browser)
    single_select.open()
    single_select.title().is_displayed()
    single_select.dropdown().is_displayed()
    single_select.submit().is_displayed()
    single_select.requirement().is_displayed()

def data():
    return [
        '1',
        '2',
        '3',
        '4',
        '5'
    ]
@allure.feature('Single_dropdown_functional')
@pytest.mark.parametrize('data',data())
def test_dropdow_select(browser,data):
    single_select = SelectSingleSelect(browser)
    single_select.open()
    single_select.title().is_displayed()
    single_select.dropdown().is_displayed()
    single_select.dropdown_select_value(data)
    single_select.should_have_selected_value(data)


def req_messages():
    return [
        'Field name is "Choose language"',
        'This is a required field',
        'User should be able to select any option',
        'The result can be sent using the Submit button',
        'After submitting the form, the option selected by the user is displayed on the page'
    ]

@allure.feature('Requirements verification')
@pytest.mark.parametrize('req_messages',req_messages())
def test_requirements(browser,req_messages):
    single_select = SelectSingleSelect(browser)
    single_select.open()
    single_select.requirement().is_displayed()
    single_select.requirement().click()
    single_select.requirements_text(req_messages).is_displayed()



