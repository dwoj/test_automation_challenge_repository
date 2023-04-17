from pages.base_page import BasePage


class AddMatchForm(BasePage):
    title_bar_header_xpath = "//*[contains(@class, 'MuiTypography-h6')]"
    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//ul[1]/div[2]/div[2]/span"
    player_account_button_xpath = "//ul[2]/div[1]/div[2]/span"
    matches_button_xpath = "//ul[2]/div[2]/div[2]/span"
    reports_button_xpath = "//div[3]/div[2]/span"
    language_button_xpath = "//ul[3]/div[1]/div[2]/span"
    sign_out_button_xpath = "//ul[3]/div[2]/div[2]/span"
    my_team_input_xpath = "//div[1]/div/div/input"
    enemy_team_input_xpath = "//div[2]/div/div/input"
    my_team_score_input_xpath = "//div[3]/div/div/input"
    enemy_team_score_input_xpath = "//div[4]/div/div/input"
    date_input_xpath = "//div[5]/div/div/input"
    match_place_xpath = "//div[6]"
    t_shirt_color_input_xpath = "//div[7]/div/div/input"
    league_input_xpath = "//div[8]/div/div/input"
    time_played_input_xpath = "//div[9]/div/div/input"
    number_input_xpath = "//div[10]/div/div/input"
    web_match_input_xpath = "//div[11]/div/div/input"
    general_input_xpath = "//div[12]/div/div/input"
    rating_input_xpath = "//div[13]/div/div/input"
    submit_button_xpath = "//div[3]/button[1]"
    clear_button_xpath = "//div[3]/button[2]"
    pass