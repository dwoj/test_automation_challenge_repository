import time
from pages.base_page import BasePage


class LoginPage(BasePage):
    main_title_xpath = "//h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    language_selector_xpath = "//div[2]/div/div"
    sign_in_button_xpath = "//*[contains(@class, 'MuiButton-label')]"
    login_url = "https://scouts.futbolkolektyw.pl/en/"
    expected_title = "Scouts panel - sign in"
    english_option = "//li[1]"
    polish_option = "//li[2]"
    expected_main_title = "Scouts Panel"
    login_error_xpath = "//div[3]/span"
    expected_error_login = "Please provide your username or your e-mail."
    expected_sign_in_button_eng = "SIGN IN"
    expected_sign_in_button_pl = "ZALOGUJ"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def select_language(self, language):
        self.click_on_the_element(self.language_selector_xpath)
        time.sleep(1)
        if language == "english":
            self.click_on_the_element(self.english_option)
        else:
            self.click_on_the_element(self.polish_option)

    def main_title_verification(self):
        self.assert_element_text(self.driver, self.main_title_xpath, self.expected_main_title)

    def error_message_verification(self):
        self.assert_element_text(self.driver, self.login_field_xpath, self.expected_error_login)

    def wait_for_login_page_view(self):
        self.wait_for_element_to_be_clickable(self.login_field_xpath)

    def assert_sign_in_button_eng(self):
        self.assert_element_text(self.driver,self.sign_in_button_xpath, self.expected_sign_in_button_eng)

    def assert_sign_in_button_pl(self):
        self.assert_element_text(self.driver,self.sign_in_button_xpath, self.expected_sign_in_button_pl)


