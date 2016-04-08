import os

# django-crispy-forms settings
# CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not True

# django-summernote settings
SUMMERNOTE_CONFIG = {
    'iframe': False,
}

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/ideas/create/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET')

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
FACEBOOK_EXTENDED_PERMISSIONS = ['picture']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, age_range'
}
