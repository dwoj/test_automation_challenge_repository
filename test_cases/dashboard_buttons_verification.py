import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_language_selector(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        time.sleep(1)
        user_login.type_in_password('Test-1234')
        time.sleep(1)
        user_login.click_on_sign_in()
        dashboard_page = Dashboard(self.driver)
        time.sleep(5)
        dashboard_page.click_on_language_selector()
        time.sleep(2)
        dashboard_page.click_on_language_selector()
        time.sleep(2)

    def test_sign_out_button(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        time.sleep(1)
        user_login.type_in_password('Test-1234')
        time.sleep(1)
        user_login.click_on_sign_in()
        dashboard_page = Dashboard(self.driver)
        time.sleep(6)
        dashboard_page.click_on_sign_out()
        time.sleep(2)
        user_login.main_title_verification()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.driver.quit()
