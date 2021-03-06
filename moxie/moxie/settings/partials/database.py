import os
import dj_database_url
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASE_URL = os.environ.get("DATABASE_URL")

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
    )
}
