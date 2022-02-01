import os
from decimal import Decimal

from django.conf import global_settings
from django.utils.translation import gettext_lazy

LANGUAGE_CODE = 'da'
COUNTRY_CODE = 'DK'
COUNTRY_NAME = "Danmark"
TIME_ZONE = 'Europe/Copenhagen'

MANDRILL_SUBACCOUNT = "MarketA.com"
BRAND_NAME = "MarketA"
MARKET_DEFAULT_CURRENCY = "DKK"
MARKET_DEFAULT_CURRENCY_SYMBOL = "kr"

INVOICE_COUNTRY_CODE = "DK"

# Set to half the width of the actual image
BRAND_EMAIL_LOGO_WIDTH = "143"

# Relative to EMAIL_ASSETS_ROOT_URL
BRAND_EMAIL_LOGO_URL = "logos/MarketA.com@2x.png"
BRAND_EMAIL_LOGO_WHITE_URL = "logos/white/MarketA.png"

ADMIN_LOGO_URL = "admin/MarketA.com@2x.png"
ADMIN_LOGO_HEIGHT = "33"

BRAND_SUPPORT_EMAIL = "info@MarketA.com"

SUPPORT_URL = "https://MarketA.zendesk.com/hc/da"

DEFAULT_FROM_EMAIL = "info@MarketA.com"
DEFAULT_FROM_NAME = "MarketA"

IMPORTER_DEFAULT_CURRENCY = "DKK"
IMPORTER_DEFAULT_IS_ANONYMOUS_CRAWLING = False

LANGUAGES = [('da', gettext_lazy('Danish')), ('en', gettext_lazy('English'))]

INVOICE_COMPANY_INFORMATION = """MarketA.com / MarketA


Some Address
8888 Some City"""

BRAND_ADDRESS = """MarketA.com / MarketA
"""

TAX_PERCENT = Decimal(os.getenv("TAX_PERCENT", "25"))

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

USE_THOUSAND_SEPARATOR = True

PASSWORD_HASHERS = global_settings.PASSWORD_HASHERS + [
    "MarketA.password_hasher.MarketAPasswordHasher"
]
BLOG_URL = "https://www.MarketA.com/blog/"
BLOG_SEEKERS_URL = "https://www.MarketA.com/blog/bblubb/"
BLOG_LANDLORDS_URL = "https://www.MarketA.com/blubb/"
BLOG_RENTOUT_URL = "https://www.MarketA.com/blog/blubb/"
JOBS_URL = "https://MarketA.com/"
FACEBOOK_URL = "https://www.facebook.com/MarketA/"
INSTAGRAM_URL = "https://www.instagram.com/MarketA/"

TRUSTPILOT_URL = 'https://com.trustpilot.com/evaluate/www.MarketA.com'
