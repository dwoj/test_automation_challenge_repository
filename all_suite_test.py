import unittest

from test_cases.change_language_in_login_page import TestChangeLanguage
from test_cases.dashboard_buttons_verification import TestDashboardButtons
from test_cases.fill_in_add_player_form import TestAddPlayer
from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage
from test_cases.open_add_player_form import TestAddPlayerForm


def full_suite():
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(makeSuite(TestChangeLanguage))
    # test_suite.addTest(makeSuite(TestDashboardButtons))
    # test_suite.addTest(makeSuite(TestAddPlayer))
    # test_suite.addTest(makeSuite(Test))
    # test_suite.addTest(makeSuite(TestLoginPage))
    # test_suite.addTest(makeSuite(TestAddPlayerForm))
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    test_suite.addTest(test_loader.loadTestsFromTestCase(TestChangeLanguage))
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestDashboardButtons))
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestAddPlayer))
    test_suite.addTest(test_loader.loadTestsFromTestCase(Test))
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestLoginPage))
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestAddPlayerForm))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
