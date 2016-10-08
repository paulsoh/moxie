import os
import raven
# django-crispy-forms settings
# CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not True

# django-summernote settings

SUMMERNOTE_CONFIG = {
    'iframe': False,
    'width': '100%',
    'external_css': (
        '/static/css/vendor/bootstrap.min.css',
    ),
    'external_js': (
        '/static/js/vendor/jquery-1.12.2.min.js',
        '/static/js/vendor/bootstrap.js',
    ),
}

"""
SUMMERNOTE_CONFIG = {
    'iframe': False,
}
"""


SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET')

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
FACEBOOK_EXTENDED_PERMISSIONS = ['picture']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, age_range'
}

RAVEN_CONFIG = {
    'dsn': 'https://df4f30e86fb14584854a466b7d64398d:9512bdb4f27f491488f1a0cae77b854e@app.getsentry.com/74130',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}
