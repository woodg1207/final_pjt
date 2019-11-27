from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='jje-0cb@1bdma166=ebahx9b95tpuub43)v%3qhrhc7f12x3q)')

DEBUG = True

ALLOWED_HOSTS = []