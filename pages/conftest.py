from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser





