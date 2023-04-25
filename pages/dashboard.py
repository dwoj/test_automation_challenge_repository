from pages.base_page import BasePage


class Dashboard(BasePage):
    title_bar_header_xpath = "//*[contains(@class, 'MuiTypography-h6')]"
    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//ul[1]/div[2]/div[2]/span"
    language_button_xpath = "//ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    players_count_label_xpath = "//div[2]/div[1]/div/div[1]"
    players_count_xpath = "//main/div[2]/div[1]/div"
    matches_count_xpath = "//div[2]/div[2]/div"
    reports_count_xpath = "//div[2]/div[3]/div"
    events_count_xpath = "//div[4]/div"
    logo_box_image_xpath = "//*[@title='Logo Scouts Panel']"
    logo_box_name_xpath = "//div[2]/h2"
    logo_box_description_xpath = "//div[2]/p"
    dev_team_contact_button_xpath = "//a/span[1]"
    shortcuts_box_name_xpath = "//div[2]/div/div/h2"
    add_player_button_xpath = "//div[2]/div/div/a/button/span[1]"
    activity_box_name_xpath = "//div[3]/div/div/h2"
    last_created_player_button_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_button_xpath = "//a[2]/button/span[1]"
    last_created_match_button_xpath = "//a[3]/button/span[1]"
    last_updated_match_button_xpath = "//a[4]/button/span[1]"
    last_updated_report_button_xpath = "//a[5]/button/span[1]"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_main_page_title = "Strona Główna"


    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.title_bar_header_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_player(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_language_selector(self):
        self.click_on_the_element(self.language_button_xpath)

    def click_on_sign_out(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def main_page_button_verification(self):
        self.assert_element_text(self.driver, self.main_page_button_xpath, self.expected_main_page_title)


