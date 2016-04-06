# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
from .application import *


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_BASE_DIR, 'dist', 'static')
MEDIA_ROOT = os.path.join(PROJECT_BASE_DIR, 'dist', 'media')

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'vendor': {
            'source_filenames': (
              'moxie/css/*.css',
            ),
            'output_filename': 'css/vendor.css',
        },
        'main': {
            'source_filenames': (
              'vanityfair/css/*.sass',
            ),
            'output_filename': 'css/moxie.min.css',
        },
    },

    'JAVASCRIPT': {
        'vendor': {
            'source_filenames': (
              'vanityfair/js/*.js',
            ),
            'output_filename': 'js/vendor.js',
        },
        'main': {
            'source_filenames': (
              'vanityfair/js/*.js',
            ),
            'output_filename': 'js/main.js',
        },
    },

    'COMPILERS': {
        'pipeline.compilers.sass.SASSCompiler',
    }
}
