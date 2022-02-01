from django.test import TestCase

from markets.market_settings.markets import MARKET_B
from markets.test_utils import override_market


class TestRedirects(TestCase):
    @override_market(MARKET_B)
    def test_market_(self):
        print("I am market b")
        self.assertTrue(True)
