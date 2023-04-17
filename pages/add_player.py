import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    title_bar_header_xpath = "//*[contains(@class, 'MuiTypography-h6')]"
    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//ul[1]/div[2]/div[2]/span"
    language_button_xpath = "//ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    email_input_xpath = "//div[1]/div/div/input"
    name_input_xpath = "//div[2]/div/div/input"
    surname_input_xpath = "//div[3]/div/div/input"
    phone_input_xpath = "//div[4]/div/div/input"
    weight_input_xpath = "//div[5]/div/div/input"
    height_input_xpath = "//div[6]/div/div/input"
    age_input_xpath = "//div[7]/div/div/input"
    leg_xpath = "//*[@id='mui-component-select-leg']"
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

    def title_of_add_player_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_page_title
