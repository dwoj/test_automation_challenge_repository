import os
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardButtons(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_language_selector(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_dashboard_view()
        dashboard_page.click_on_language_selector()
        dashboard_page.assert_main_page_pl()

    def test_sign_out_button(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_dashboard_view()
        dashboard_page.click_on_sign_out()
        user_login.wait_for_login_page_view()
        user_login.main_title_verification()

    @classmethod
    def tearDown(self):
        self.driver.quit()
