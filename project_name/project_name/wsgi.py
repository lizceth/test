"""
WSGI config for project_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os
from os.path import abspath, dirname, basename, join, normpath
from sys import path
import os

from django.core.wsgi import get_wsgi_application

SITE_ROOT=dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")

application = get_wsgi_application()
