from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open(self):
        return self.browser.get('https://practice-automation.com/')

    #Locators главной страницы https://practice-automation.com/

    def header_picture(self):
        return self.browser.find_element(By.XPATH, '//img[@alt="automateNow Logo"]')

    def courses_link(self):
        return self.browser.find_element(By.XPATH, '//span[@data-hover="Courses"]')

    def blog_link(self):
        return self.browser.find_element(By.XPATH, '//span[@data-hover="Blog"]')

    def learn_more_link(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "Learn More")]')

    def about_link(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "About")]')

    def welcome_text(self):
        return self.browser.find_element(By.XPATH,
                                         '//strong[contains(text(), "Welcome to your software automation practice website! ")]')

    def page_text(self):
        return self.browser.find_element(By.XPATH,
                                         '//strong[contains(text(), "We have developed this site as a one-stop place to practice web automation. You can find additional")]')

    def java_script_delays_button(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "JavaScript Delays")]')

    def form_field_button(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "Form Fields")]')

    def popups_button(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "Popups")]')

    def sliders_button(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "Sliders")]')

    def tables_button(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "Tables")]')

    def window_operation_button(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "Window Operations")]')

    def hover_button(self):
        return self.browser.find_element(By.XPATH, '//a[contains(text(), "Hover")]')







