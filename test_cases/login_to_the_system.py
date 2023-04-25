import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        time.sleep(1)
        user_login.type_in_password('Test-1234')
        time.sleep(1)
        user_login.click_on_sign_in()
        time.sleep(1)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    def test_log_in_to_the_system_invalid_data(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        time.sleep(1)
        user_login.type_in_password('Test-12345678')
        time.sleep(1)
        user_login.click_on_sign_in()
        time.sleep(2)
        user_login.main_title_verification()
        time.sleep(4)


    @classmethod
    def tearDown(self):
        self.driver.quit()
