import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Users/nikitanicvetov/PycharmProjects/Test Project')
from qaPractice.methods.main_page_1 import MainPage


def test_page_elements_is_presented(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.header_picture().is_displayed()
    main_page.courses_link().is_displayed()
    main_page.blog_link().is_displayed()
    main_page.learn_more_link().is_displayed()
    main_page.about_link().is_displayed()
    main_page.welcome_text().is_displayed()
    main_page.page_text().is_displayed()
    main_page.java_script_delays_button().is_displayed()
    main_page.form_field_button().is_displayed()
    main_page.popups_button().is_displayed()
    main_page.sliders_button().is_displayed()
    main_page.tables_button().is_displayed()
    main_page.window_operation_button().is_displayed()
    main_page.hover_button().is_displayed()
