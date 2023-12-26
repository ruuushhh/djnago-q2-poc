"""
Django settings for django_poc project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import sys

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DEBUG') == 'True' else False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY')


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Installed Apps
    'rest_framework',
    'corsheaders',
    'django_q',
    'apps.users',

]

MIDDLEWARE = [
    'request_logging.middleware.LoggingMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_poc.urls"
APPEND_SLASH = False

AUTH_USER_MODEL = 'users.User'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

FYLE_REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'apps.users.serializers.UserSerializer'
}

FYLE_REST_AUTH_SETTINGS = {
    'async_update_user': True
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        # 'apps.workspaces.permissions.WorkspacePermissions'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'fyle_rest_auth.authentication.FyleJWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'auth_cache',
    }
}

# Q_CLUSTER = {
#     'name': 'django_poc',
#     'save_limit': 0,
#     'retry': 14400, #4 hours
#     'timeout': 3600, #1 hour
#     'catch_up': False,
#     'workers': 4,
#     # How many tasks are kept in memory by a single cluster.
#     # Helps balance the workload and the memory overhead of each individual cluster
#     'queue_limit': 10,
#     'cached': False,
#     'orm': 'default',
#     'ack_failures': True,
#     'poll': 1,
#     'max_attempts': 1,
#     'attempt_count': 1,
#     # The number of tasks a worker will process before recycling.
#     # Useful to release memory resources on a regular basis.
#     'recycle': 50,
#     # The maximum resident set size in kilobytes before a worker will recycle and release resources.
#     # Useful for limiting memory usage.
#     'max_rss': 100000  # 100mb
# }

# Q_CLUSTER settings (no BROKER_URL needed for ORM)
Q_CLUSTER = {
    'name': 'django_poc',
    'save_limit': 0,
    'retry': 14400,  # 4 hours
    'timeout': 3600,  # 1 hour
    'catch_up': False,
    'workers': 4,
    'queue_limit': 10,
    'cached': False,
    'orm': 'default',  # Indicate ORM as the broker
    'ack_failures': True,
    'poll': 1,
    'max_attempts': 1,
    'attempt_count': 1,
    'recycle': 50,
    'max_rss': 100000,  # 100mb
    'ALT_CLUSTERS': {
        'import_tasks': {
            'workers': 2,
            'recycle': 50,
            'max_rss': 100000,
        },  # No need to specify 'orm' here, it will use 'default'
        'export_tasks': {
            'workers': 2,
            'recycle': 50,
            'max_rss': 100000,
        },  # No need to specify 'orm' here either
    }
}


WSGI_APPLICATION = 'django_poc.wsgi.application'

SERVICE_NAME = os.environ.get('SERVICE_NAME')


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# Defaulting django engine for qcluster
if len(sys.argv) > 0 and sys.argv[1] == 'qcluster':
    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    DATABASES = {
        'default': dj_database_url.config(engine='django_db_geventpool.backends.postgresql_psycopg2')
    }

DATABASES['cache_db'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'cache.db'
}

DATABASE_ROUTERS = ['django_poc.cache_router.CacheRouter']


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = ['sentry-trace', 'authorization', 'content-type']