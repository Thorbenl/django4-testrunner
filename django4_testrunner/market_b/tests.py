from django.test import TestCase

from django4_testrunner.default.market_settings import override_market, MARKET_B


class TestRedirects(TestCase):
    @override_market(MARKET_B)
    def test_simple(self):
        print(MARKET_B)
        self.assertTrue(True)
