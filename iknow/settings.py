"""
Django settings for iknow project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import pathlib
import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG_BOOL")
print(type(DEBUG))
ALLOWED_HOSTS = ['127.0.0.1', 'deepsyntax.org', 'www.deepsyntax.org', '24.199.106.171']




# Application definition

INSTALLED_APPS = [
    'taggit',
    'blog.apps.BlogConfig',
    ## Enable in production mode
    'my_user',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'tailwind',
    'themetailwind',
       
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG == True:
    INSTALLED_APPS += "django_browser_reload"
    MIDDLEWARE += "django_browser_reload.middleware.BrowserReloadMiddleware"

ROOT_URLCONF = 'iknow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            pathlib.Path(BASE_DIR,r'templates'),
            pathlib.Path(BASE_DIR,r'themetailwind\templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iknow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if DEBUG == "True":
    print(DEBUG, "tailwind development for database")
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'iknowblog.sqlite3',
        }
    }
    NPM_BIN_PATH=r"C:\Program Files\nodejs\npm.cmd"
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
else:
    DATABASES = {
    ## Enable postgres when in production mode

        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('DATABASE_NAME'),
            'USER': env('DATABASE_USER'),
            'PASSWORD': env('DATABASE_PASSWORD'),
            'HOST': env('DATABASE_HOST'),
            'PORT': env("DATABASE_PORT")
        }
    }
    print(DEBUG, "tailwind Production")
    NPM_BIN_PATH=(r"npm")
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



DEFAULT_AUTO_FIELD = 'django.db.models.AutoField' 
TAGGIT_CASE_INSENSITIVE = True

# ## Enable auth when in production mode

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
# STATICFILES_DIRS = [
#      os.path.join(BASE_DIR, 'static'),
   
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'my_user.User'

TAILWIND_APP_NAME = 'themetailwind'



TINYMCE_DEFAULT_CONFIG = {

   'height': 560,
   'width': 1120,
   'cleanup_on_startup': True,
   'custom_undo_redo_levels': 20,
   'selector': 'textarea',
   'theme': 'silver',
   'plugins': '''
   textcolor save link image media preview codesample contextmenu
   table code advlist lists fullscreen insertdatetime nonbreaking
   directionality searchreplace wordcount visualblocks visualchars
   autolink  charmap print hr anchor pagebreak paste  help  
   spellchecker
   ''',
   'toolbar1': '''
   fullscreen preview bold italic underline | styleselect fontselect,
   fontsizeselect | forecolor backcolor | alignleft alignright |
   aligncenter alignjustify | indent outdent | bullist numlist table |
   | link image media | codesample | removeformat | help
   ''',
   'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor | code |
            ''',
   'contextmenu': 'formats | link image',
   'menubar': True,
   'statusbar': True,
   'style_formats': [
            {'title':'numlist', 'items': [{'list-style-type':'armanian',}]},
    ]
   }


TINYMCE_SPELLCHECKER = True
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "/tinymce")
# TINYMCE_JS_URL = 'http://cdn.tinymce.com/4/tinymce.min.js'
# TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/arhsp0g09j7sgm4c0n24ce7t2j5ludxxy8ul3r5xcdpiwmh5/tinymce/5/tinymce.min.js'
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
TINYMCE_COMPRESSOR = False
# TINYMCE_EXTRA_MEDIA = {'css': {'all': []},'js':[]}