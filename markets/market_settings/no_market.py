import os
from decimal import Decimal

from django.utils.translation import gettext_lazy

LANGUAGE_CODE = 'da'
COUNTRY_CODE = 'DK'
COUNTRY_NAME = "Danmark"
TIME_ZONE = 'Europe/Copenhagen'

MANDRILL_SUBACCOUNT = "nomarket"
BRAND_NAME = "NoMarket"
MARKET_DEFAULT_CURRENCY = "DKK"
MARKET_DEFAULT_CURRENCY_SYMBOL = "kr"


# Set to half the width of the actual image
BRAND_EMAIL_LOGO_WIDTH = "143"

# Relative to EMAIL_ASSETS_ROOT_URL
BRAND_EMAIL_LOGO_URL = "logos/no_market@2x.png"
BRAND_EMAIL_LOGO_WHITE_URL = ""

ADMIN_LOGO_URL = "admin/no_market@2x.png"
ADMIN_LOGO_HEIGHT = "33"

BRAND_SUPPORT_EMAIL = "info@example.com"

SUPPORT_URL = "https://en.wikipedia.org/wiki/Cat"

DEFAULT_FROM_EMAIL = "info@example.com"
DEFAULT_FROM_NAME = "NoMarket"


IMPORTER_DEFAULT_CURRENCY = "DKK"
IMPORTER_DEFAULT_IS_ANONYMOUS_CRAWLING = False

LANGUAGES = [('da', gettext_lazy('Danish')),
             ('sv', gettext_lazy('Swedish')),
             ('de', gettext_lazy('German')),
             ('en', gettext_lazy('English'))]


TAX_PERCENT = Decimal(os.getenv("TAX_PERCENT", "25"))

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

USE_THOUSAND_SEPARATOR = True


# END Market-specific settings

PHONENUMBER_DEFAULT_REGION = 'DK'


BLOG_URL = "https://en.wikipedia.org/wiki/Cat"
BLOG_SEEKERS_URL = "https://en.wikipedia.org/wiki/Cat"
BLOG_LANDLORDS_URL = "https://en.wikipedia.org/wiki/Cat"
BLOG_RENTOUT_URL = "https://en.wikipedia.org/wiki/Cat"
JOBS_URL = "https://en.wikipedia.org/wiki/Cat"
FACEBOOK_URL = "https://en.wikipedia.org/wiki/Facebook"
INSTAGRAM_URL = "https://en.wikipedia.org/wiki/Instagram"

