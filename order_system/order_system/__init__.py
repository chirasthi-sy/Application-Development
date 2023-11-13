import os
from django.core.wsgi import get_wsgi_application


from django.apps import apps
from django.conf import settings

apps.populate(settings.INSTALLED_APPS)
