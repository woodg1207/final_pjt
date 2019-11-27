from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['movie-hospital.upuxkamv6m.ap-northeast-2.elasticbeanstalk.com']