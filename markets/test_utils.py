import contextlib
import os

from django.test.utils import tag

from markets.market_settings.markets import valid_market


def override_market(market):
    if not valid_market(market):
        raise Exception(f"{market} is not a valid market.")
    return tag(market)


@contextlib.contextmanager
def override_env(**environ):
    old_environ = dict(os.environ)
    os.environ.update(environ)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_environ)