from django.test import TestCase
from market_a_app.models import AdvertisementIdMapping
from markets.market_settings.markets import MARKET_A
from markets.test_utils import override_market


class TestRedirects(TestCase):
    @override_market(MARKET_A)
    def test_market_a(self):
        ad = AdvertisementIdMapping.objects.create(advertisement_id=6071144)
        print(type(ad))
        print("I am market a")
        self.assertTrue(True)





