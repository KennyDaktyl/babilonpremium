"""

Django settings for pizzeria project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATICFILES_DIRS = (os.path.join(SITE_ROOT, "static"),)

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = (os.environ.get("SECRET_KEY"),)
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = [
    "*",
]


import socket

print(socket.gethostname())

if socket.gethostname() == "Asus":
    SECURE_SSL_REDIRECT = False
    DEBUG = True
    
    DATABASES = {
    "default": {
        "NAME": "babilon_02",
        "ENGINE": "django.db.backends.postgresql",
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": "localhost",
    }
}
else:
    SECURE_SSL_REDIRECT = True
    DEBUG = bool(os.environ.get("DEBUG_VALUE") == "False")
    DATABASES = {
    "default": {
        "NAME": "premium03",
        "ENGINE": "django.db.backends.postgresql",
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": "localhost",
    }
}


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "babilon_v1",
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    # 'django_extensions', # rysowanie diagramu database
]

# disable view restapi without authorisation
REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    # ]
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ]
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pizzeria.urls"

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

WSGI_APPLICATION = "pizzeria.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# import dj_database_url

# PG_URL = os.environ.get("DATABASE_URL")
# DATABASES = {"default": dj_database_url.config(default=PG_URL)}


# DATABASES = {
#     "default": {
#         "NAME": "premium03",
#         "ENGINE": "django.db.backends.postgresql",
#         "USER": os.environ.get("DB_USER"),
#         "PASSWORD": os.environ.get("DB_PASSWORD"),
#         "HOST": "localhost",
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]
AUTH_USER_MODEL = "babilon_v1.MyUser"
TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/pizzeria/static/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "pizzeria/static/media/")

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LANGUAGE_CODE = "pl"

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = "pizzeria/static/media/"

# MEDIA_ROOT = os.path.join(BASE_DIR, "static/media/")

LOGIN_URL = "/login/"

SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DATETIME_FORMAT = "Y-m-d H:M:S"
USE_L10N = True
USE_TZ = True
TIME_ZONE = "Poland"

CRISPY_TEMPLATE_PACK = "bootstrap4"

django_heroku.settings(locals())

# import dj_database_url
# DATABASES = {
#     "default": dj_database_url.config(
#         default="postgres://postgres:Tofik123!@51.75.127.94:5432/pizzeria"
#     )
# }
