import os

from vcp_backend.settings.base import ALLOWED_HOSTS
from . import prod_database

DEBUG = True

DATABASES = prod_database.DATABASE_SETTING

ALLOWED_HOSTS=['*']