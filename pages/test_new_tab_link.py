from new_tab_link import NewTabLink
import allure
import pytest

@allure.feature('Page elements')
def test_page_elements(browser):
    new_tab_link_page = NewTabLink(browser)
    new_tab_link_page.open()
    new_tab_link_page.link_text().is_displayed()
    new_tab_link_page.requirement().is_displayed()

@allure.feature('Open new tab')
def test_open_new_page(browser):
    new_tab_link_page = NewTabLink(browser)
    new_tab_link_page.open()
    new_tab_link_page.link_text().click()
    new_tab_link_page.new_page()
    assert 'https://www.qa-practice.com/elements/new_tab/new_page' == new_tab_link_page.get_page_url()
    new_tab_link_page.sucsess_message().is_displayed()

def request_mesages():
    return[
        'The link should open the page /elements/new_tab/new_page',
        'New page should be opened in a new tab'
    ]
@allure.feature('Requirement')
@pytest.mark.parametrize('request_mesages', request_mesages())
def test_requirement(browser, request_mesages):
    new_tab_link_page = NewTabLink(browser)
    new_tab_link_page.open()
    new_tab_link_page.requirement().is_displayed()
    new_tab_link_page.requirement().click()
    new_tab_link_page.requirements_text(request_mesages)

