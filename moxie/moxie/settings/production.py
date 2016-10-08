import os

from .partials import *


ALLOWED_HOSTS = [
    '*',
]

DEBUG = False

STATICFILES_STORAGE = 'moxie.storage.S3PipelineCachedStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_HOST = "s3-ap-northeast-1.amazonaws.com"

AWS_S3_CUSTOM_DOMAIN = 'd2ya8x6fgqaj6c.cloudfront.net'

AWS_S3_URL_PROTOCOL = 'https'

STATIC_URL = "https://d2ya8x6fgqaj6c.cloudfront.net/"
