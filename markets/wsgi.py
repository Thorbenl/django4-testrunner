"""
WSGI config for newmarkets project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "markets.settings")

application = get_wsgi_application()

# Disabled warm-up since this causes issues with New Relic: https://docs.newrelic.com/docs/agents/python-agent/web-frameworks-servers/python-agent-gunicorn-wsgi-web-server#preloading-applications
# # Django warm-up ahead of time instead of lazy
# # From: http://uwsgi-docs.readthedocs.org/en/latest/articles/TheArtOfGracefulReloading.html#dealing-with-ultra-lazy-apps-like-django
# #  And: https://github.com/stefantalpalaru/uwsgi_reload/blob/master/examples/wsgi.py#L19
# application({
#     'REQUEST_METHOD': 'GET',
#     'SERVER_NAME': '127.0.0.1',
#     'SERVER_PORT': 80,
#     'PATH_INFO': '/',
#     'wsgi.input': sys.stdin,
# }, lambda x, y: None)
#
# Close connections before forking
from django.db import connections

for conn in connections.all():
    conn.close()