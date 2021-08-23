import unittest

from datetime import datetime, timedelta
from unittest import mock
from unittest.mock import patch, Mock

from exercises.promo.promo import Promo


class TestExpired(unittest.TestCase):

    NOW = datetime.now()

    def test_valid(self):
        yesterday = self.NOW - timedelta(days=1)
        instance = Promo('', yesterday)
        response = instance.expired
        self.assertEqual(response, True)


    def test_expired(self):
        tomorrow = self.NOW + timedelta(days=1)
        instance = Promo('',tomorrow)
        response = instance.expired
        self.assertEqual(response, False)


    def test_property_exist(self):
        self.assertTrue(hasattr(Promo, 'expired'))