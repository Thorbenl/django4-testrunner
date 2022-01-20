from django.test.utils import tag

MARKET_A = "MARKET_A"
MARKET_B = "MARKET_B"


def override_market(market):
    if not valid_market(market):
        raise Exception(f"{market} is not a valid market.")
    return tag(market)


def valid_market(market: str):
    return market in [MARKET_A, MARKET_B]
