"""
Django settings for django4_testrunner project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import sys
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+!$p@nek)^^b2n#o$=$l1-*2x*0nn8c!jrr!)rkf-zo&1i*=32'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'default'
]

RUNNING_TESTS = sys.argv[1:2] == ['test']
MARKET: Optional[str]
if RUNNING_TESTS:
    MARKET = os.environ.get("MARKET", "MARKET_A")
else:
    # If MARKET is not provided, use None as "market", which means all market-specific apps will be included.
    # This is useful when making all migrations, compiling translations, or type-checking with mypy.
    MARKET = os.environ.get("MARKET", None)

if MARKET not in ["MARKET_A", "MARKET_B"]:
    raise Exception("Unknown market")

MARKET_SPECIFIC_APPS = {
    "MARKET_A": [
        'market_a.apps.MarketAConfig',
    ],
    "MARKET_B": [
        'market_b.apps.MarketBConfig',
    ],
}

if MARKET in MARKET_SPECIFIC_APPS:
    # If there is a market-specific app, add it to INSTALLED_APPS
    INSTALLED_APPS += MARKET_SPECIFIC_APPS[MARKET]

if MARKET is None:
    # If making migrations, include all apps so all migrations are generated
    # No market is also used for type checking. If it doesn't include all apps, it will complain
    for market in MARKET_SPECIFIC_APPS:
        INSTALLED_APPS += MARKET_SPECIFIC_APPS[market]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if RUNNING_TESTS:
    # Use a fast password hasher when running tests.
    # See https://docs.djangoproject.com/en/2.1/topics/testing/overview/#password-hashing
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]

ROOT_URLCONF = 'django4_testrunner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django4_testrunner.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'