import os
from decimal import Decimal

from django.conf import global_settings
from django.utils.translation import gettext_lazy

LANGUAGE_CODE = 'sv'
COUNTRY_CODE = 'SE'
COUNTRY_NAME = "Sverige"
TIME_ZONE = 'Europe/Stockholm'

BRAND_NAME = "MarketB"
MARKET_DEFAULT_CURRENCY = "SEK"
MARKET_DEFAULT_CURRENCY_SYMBOL = "kr"


# Set to half the width of the actual image
BRAND_EMAIL_LOGO_WIDTH = "143"

# Relative to EMAIL_ASSETS_ROOT_URL
BRAND_EMAIL_LOGO_URL = "logos/market_b@2x.png"
BRAND_EMAIL_LOGO_WHITE_URL = "logos/white/MarketB.png"

ADMIN_LOGO_URL = "admin/market_b@2x.png"
ADMIN_LOGO_HEIGHT = "33"

BRAND_SUPPORT_EMAIL = "info@market_b"

SUPPORT_URL = "https://support.market_b/hc/sv"

DEFAULT_FROM_EMAIL = "info@market_b"
DEFAULT_FROM_NAME = "MarketB"

IMPORTER_DEFAULT_CURRENCY = "SEK"
IMPORTER_DEFAULT_IS_ANONYMOUS_CRAWLING = True

LANGUAGES = [('sv', gettext_lazy('Swedish')), ('en', gettext_lazy('English'))]

INVOICE_COMPANY_INFORMATION = """MarketB.com / MarketB


Some Address
8888 Some City"""

BRAND_ADDRESS = """MarketB.com / MarketB
"""

TAX_PERCENT = Decimal(os.getenv("TAX_PERCENT", "25"))

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

USE_THOUSAND_SEPARATOR = True


PHONENUMBER_DEFAULT_REGION = 'SE'


PASSWORD_HASHERS = global_settings.PASSWORD_HASHERS + [
    "MarketB.password_hasher.MarketBPasswordHasher"
]
BLOG_URL = "https://market_b/blogg/"
BLOG_SEEKERS_URL = "https://market_b/blogg/rergf/"
BLOG_LANDLORDS_URL = "" #
BLOG_RENTOUT_URL = "https://market_b/blogg/erferf/"
JOBS_URL = "" #
FACEBOOK_URL = "https://www.facebook.com/MarketB"
INSTAGRAM_URL = "https://www.instagram.com/MarketB/"

TRUSTPILOT_URL = 'https://www.trustpilot.com/evaluate/market_b'
