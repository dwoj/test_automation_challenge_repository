import os
import time
import unittest
from selenium import webdriver

from pages.add_player_form import AddPlayer
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

    def test_add_player_full_details(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        time.sleep(1)
        user_login.type_in_password('Test-1234')
        time.sleep(1)
        user_login.click_on_sign_in()
        dashboard_page = Dashboard(self.driver)
        time.sleep(3)
        dashboard_page.click_on_add_player()
        add_player_page = AddPlayer(self.driver)
        add_player_page.title_of_add_player_page()
        add_player_page.type_in_name('Jan')
        time.sleep(1)
        add_player_page.type_in_surname('Nowak')
        time.sleep(1)
        add_player_page.type_in_age('01-03-2003')
        time.sleep(1)
        add_player_page.click_on_leg_field()
        time.sleep(1)
        add_player_page.click_on_right_leg()
        time.sleep(1)
        add_player_page.type_in_main_position('goalkeeper')
        add_player_page.click_on_submit_button()
        time.sleep(4)

    def test_add_player_missing_data(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        time.sleep(1)
        user_login.type_in_password('Test-1234')
        time.sleep(1)
        user_login.click_on_sign_in()
        dashboard_page = Dashboard(self.driver)
        time.sleep(3)
        dashboard_page.click_on_add_player()
        add_player_page = AddPlayer(self.driver)
        add_player_page.title_of_add_player_page()
        add_player_page.type_in_name('Jan')
        time.sleep(1)
        add_player_page.type_in_surname('Nowak')
        time.sleep(1)
        add_player_page.type_in_age('01-03-2003')
        time.sleep(2)
        add_player_page.click_on_submit_button()
        time.sleep(3)

    def test_clear_button(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        time.sleep(1)
        user_login.type_in_password('Test-1234')
        time.sleep(1)
        user_login.click_on_sign_in()
        dashboard_page = Dashboard(self.driver)
        time.sleep(3)
        dashboard_page.click_on_add_player()
        add_player_page = AddPlayer(self.driver)
        add_player_page.title_of_add_player_page()
        add_player_page.type_in_name('Jan')
        time.sleep(1)
        add_player_page.type_in_surname('Nowak')
        time.sleep(1)
        add_player_page.type_in_age('01-03-2003')
        time.sleep(1)
        add_player_page.type_in_main_position('goalkeeper')
        time.sleep(2)
        add_player_page.click_on_clear_button()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.driver.quit()
