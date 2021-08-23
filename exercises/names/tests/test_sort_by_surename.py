import unittest

from unittest.mock import patch

from exercises.names import services

@patch('exercises.names.services.clean_and_title_case_names')
class TestSortBySurename(unittest.TestCase):

    NAMES = ['Alec baldwin', 'arnold Schwarzenegger' ]
    NAMES_UPPERCASE = ['Alec Baldwin', 'Arnold Schwarzenegger' ]
    NAMES_SORTED = ['Arnold Schwarzenegger', 'Alec Baldwin']
    ADDITIONAL_NAME = 'Oscar Schwarzenegger'

    def test_only_sort(self, mock_clean):
        mock_clean.return_value = self.NAMES_UPPERCASE
        response = services.sort_by_surename(self.NAMES)
        self.assertEqual(response, self.NAMES_SORTED)


    def test_surename_duplicated(self, mock_clean):
        names = self.NAMES
        names.append(self.ADDITIONAL_NAME)
        cleaned_names = self.NAMES_UPPERCASE
        cleaned_names.append(self.ADDITIONAL_NAME)
        expected_response = [self.ADDITIONAL_NAME]
        expected_response.extend(self.NAMES_SORTED)
        mock_clean.return_value = self.NAMES_UPPERCASE
        response = services.sort_by_surename(names)
        self.assertEqual(response, expected_response)
