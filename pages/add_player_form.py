import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    title_bar_header_xpath = "//*[contains(@class, 'MuiTypography-h6')]"
    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//ul[1]/div[2]/div[2]/span"
    language_button_xpath = "//ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    main_page_title_xpath = "//form/div[1]/div/span"
    email_input_xpath = "//div[1]/div/div/input"
    name_input_xpath = "//div[2]/div/div/input"
    surname_input_xpath = "//div[3]/div/div/input"
    phone_input_xpath = "//div[4]/div/div/input"
    weight_input_xpath = "//div[5]/div/div/input"
    height_input_xpath = "//div[6]/div/div/input"
    age_input_xpath = "//div[7]/div/div/input"
    leg_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//li[1]"
    club_input_xpath = "//div[9]/div/div/input"
    level_input_xpath = "//div[10]/div/div/input"
    main_position_input_xpath = "//div[11]/div/div/input"
    second_position_input_xpath = "//div[12]/div/div/input"
    achievements_input_xpath = "//div[14]/div/div/input"
    add_language_button_xpath = "//div[15]/button/span[1]"
    add_link_to_youtube_button_xpath = "//div[19]/button/span[1]"
    submit_button_xpath = "//div[3]/button[1]/span[1]"
    clear_button_xpath = "//button[2]/span[1]"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_page_title = "Add player"
    required_field_message_xpath = "//div[11]/div/p"
    expected_required_field_message = "Required"

    def title_of_add_player_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_page_title

    def type_in_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_input_xpath, age)

    def click_on_leg_field(self):
        self.click_on_the_element(self.leg_xpath)

    def click_on_right_leg(self):
        self.click_on_the_element(self.right_leg_xpath)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_input_xpath, main_position)

    def click_on_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def click_on_main_page_button(self):
        self.click_on_the_element(self.main_page_button_xpath)

    def assert_required_field(self):
        self.assert_element_text(self.driver, self.required_field_message_xpath, self.expected_required_field_message)

