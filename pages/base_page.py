from selenium.webdriver.ie.webdriver import WebDriver




class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)
