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
                'css/vendor/bootstrap-social.css',
                'css/vendor/fileinput.min.css',
                'css/vendor/slider.css',
                'css/vendor/datepicker.css',
            ),
            'output_filename': 'css/vendor.css',
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
            ),
            'output_filename': 'js/vendor.js',
        },
        'plugins': {
            'source_filenames': (
              'js/vendor/jquery.simplyscroll.js',
              'js/vendor/bootstrap.js',
              'js/vendor/fileinput.js',
              'js/vendor/bootstrap-slider.js',
              'js/vendor/bootstrap-datepicker.js',
            ),
            'output_filename': 'js/plugins.js',
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
        'update': {
            'source_filenames': (
              'js/update_idea.js',
            ),
            'output_filename': 'js/update_idea.js',
        },
        'create': {
            'source_filenames': (
              'js/create_idea.js',
            ),
            'output_filename': 'js/create_idea.js',
        },
    },

    'COMPILERS': {
        'pipeline.compilers.sass.SASSCompiler',
    },
}

PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
