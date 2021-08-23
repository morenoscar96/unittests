import unittest

from exercises.names import services

class TestFindShortestName(unittest.TestCase):

    NAMES = ['arnold Schwarzenegger', 'Alec baldwin']

    def test_get_shortest_name(self):
        response = services.find_shortest_name(self.NAMES)
        self.assertEqual(response, 'Alec')
