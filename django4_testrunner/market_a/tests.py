import os

from django.test import TestCase

from django4_testrunner.default.market_settings import override_market, MARKET_A


class TestRedirects(TestCase):
    print("hello")
    print(os.environ.get("MARKET"))
    @override_market(MARKET_A)
    def test_simple(self):
        print(MARKET_A)
        self.assertTrue(True)
