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
                'css/vendor/bootstrap.min.css',
                'css/vendor/jquery.simplyscroll.css',
                'css/vendor/font-awesome.min.css',
            ),
            'output_filename': 'css/bootstrap.min.css',
        },
        'moxie': {
            'source_filenames': (
                'sass/moxie.sass',
            ),
            'output_filename': 'css/moxie.min.css',
        },
    },

    'JAVASCRIPT': {
        'vendor': {
            'source_filenames': (
              'js/vendor/jquery-1.12.2.min.js',
              'js/vendor/bootstrap.js',
              'js/vendor/jquery.simplyscroll.js',
            ),
            'output_filename': 'js/vendor.js',
        },
        'moxie': {
            'source_filenames': (
              'js/myApp.js',
            ),
            'output_filename': 'js/main.js',
        },
        'detail': {
            'source_filenames': (
              'js/detail_fund.js',
            ),
            'output_filename': 'js/detail_fund.js',
        },
    },

    'COMPILERS': {
        'pipeline.compilers.sass.SASSCompiler',
    },
}

PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
