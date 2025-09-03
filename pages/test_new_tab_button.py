from new_tab_button import NewTabButton
import allure
import pytest

@allure.feature('Page elements')
def test_page_button_elements(browser):
    new_tab_button_page = NewTabButton(browser)
    new_tab_button_page.open()
    new_tab_button_page.button().is_displayed()
    new_tab_button_page.requirement().is_displayed()

@allure.feature('Open new tab')
def test_open_new_page(browser):
    new_tab_button_page = NewTabButton(browser)
    new_tab_button_page.open()
    new_tab_button_page.button().click()
    new_tab_button_page.new_page()
    assert 'https://www.qa-practice.com/elements/new_tab/new_page' == new_tab_button_page.get_page_url()
    new_tab_button_page.sucsess_message().is_displayed()


def require_message():
    return[
        'The button should open the page /elements/new_tab/new_page',
        'New page should be opened in a new tab'
    ]
@allure.feature('Requirement')
@pytest.mark.parametrize('require_message', require_message())
def test_requirement1(browser, require_message):
    new_tab_button_page = NewTabButton(browser)
    new_tab_button_page.open()
    new_tab_button_page.requirement().click()
    new_tab_button_page.requirements_text(require_message)

