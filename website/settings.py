from pathlib import Path
from dotenv import load_dotenv
import os
import boto3
from storages.backends.s3boto3 import S3Boto3Storage
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = os.environ['SECRET_KEY']

SECRET_KEY = 'django-insecure-qy9dv^yyw+po8t-kk+icam2k2c_or5g9f)$gsir#58l+n1nn-#'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quotesapp',
    'django_social_share'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'quotesapp.context_processors.common_data'
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ['PGDATABASE'],
#         'USER': os.environ['PGUSER'],
#         'PASSWORD': os.environ['PGPASSWORD'],
#         'HOST': os.environ['PGHOST'],
#         'PORT': os.environ['PGPORT']
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


AWS_ACCESS_KEY_ID = 'AKIAXPZBQGU33FLEYPTR'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'book-info'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_DEFAULT_ACL = 'public-read'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
# AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']
# AWS_DEFAULT_ACL = os.environ['AWS_DEFAULT_ACL']
# DEFAULT_FILE_STORAGE = os.environ['DEFAULT_FILE_STORAGE']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
