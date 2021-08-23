import unittest

from exercises.names import services

class TestCleanAndTitleCaseNames(unittest.TestCase):

    NAMES = ['arnold Schwarzenegger', 'Alec baldwin']
    NAMES_UPPERCASE = ['Arnold Schwarzenegger', 'Alec Baldwin']


    def test_names_no_duplicated(self):
        response = services.clean_and_title_case_names(self.NAMES)
        self.assertEqual(response, self.NAMES_UPPERCASE)


    def test_names_duplicated(self):
        names = self.NAMES * 2
        response = services.clean_and_title_case_names(names)
        self.assertEqual(response, self.NAMES_UPPERCASE)
