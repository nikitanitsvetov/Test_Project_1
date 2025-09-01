from select_multiple_select import MultipleSelect
import pytest
import allure


def page_text():
    return [
        'Choose the place you want to go',
        'Choose how you want to get there',
        'Choose when you want to go',
    ]
@allure.feature('Verify text page')
@pytest.mark.parametrize('page_text', page_text())
def test_page_text_visible(browser, page_text):
    multiple_select_page = MultipleSelect(browser)
    multiple_select_page.open()
    multiple_select_page.page_text(page_text).is_displayed()

def data():
    return [
        '1',
        '2',
        '3',
        '4',
        '5'
    ]
@allure.feature('Verify fist Dropdown')
@pytest.mark.parametrize('data',data())
def test_dropdow_select1(browser,data):
    multiple_select_page = MultipleSelect(browser)
    multiple_select_page.open()
    multiple_select_page.dropdown1().is_displayed()
    multiple_select_page.dropdown_select_value1(data)
    multiple_select_page.should_have_selected_value1(data)

@allure.feature('Verify second Dropdown')
@pytest.mark.parametrize('data',data()[:4])
def test_dropdow_select2(browser,data):
    multiple_select_page = MultipleSelect(browser)
    multiple_select_page.open()
    multiple_select_page.dropdown2().is_displayed()
    multiple_select_page.dropdown_select_value2(data)
    multiple_select_page.should_have_selected_value2(data)

@allure.feature('Verify third Dropdown')
@pytest.mark.parametrize('data',data()[:3])
def test_dropdow_select3(browser,data):
    multiple_select_page = MultipleSelect(browser)
    multiple_select_page.open()
    multiple_select_page.dropdown3().is_displayed()
    multiple_select_page.dropdown_select_value3(data)
    multiple_select_page.should_have_selected_value3(data)

@allure.feature('VWork Dropdown')
def test_dropdown_multi_select(browser):
    multiple_select_page = MultipleSelect(browser)
    multiple_select_page.open()
    multiple_select_page.dropdown_select_random_value1()
    multiple_select_page.dropdown_select_random_value2()
    multiple_select_page.dropdown_select_random_value3()
    multiple_select_page.submit().click()
    multiple_select_page.submit_message().is_displayed()

def request_mesages():
    return[
        'There should be 3 fields:',
        'Choose the place you want to go',
        'Choose how you want to get there',
        'Choose when you want to go',
        'All the fields are required',
        'User should be able to select any option in each field',
        'The result can be sent using the Submit button',
        'After submitting the form, the option selected by the user should be placed into the resulting phrase and displayed to the user',
        'Resulting phrase template: "to go by <transport> to the <destination> <when>"'
    ]
@allure.feature('Requirement')
@pytest.mark.parametrize('request_mesages', request_mesages())
def test_requirement(browser, request_mesages):
    multiple_select_page = MultipleSelect(browser)
    multiple_select_page.open()
    multiple_select_page.requirement().is_displayed()
    multiple_select_page.requirement().click()
    multiple_select_page.requirements_text(request_mesages)