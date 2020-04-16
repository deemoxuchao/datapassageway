"""
Django settings for datapassageway project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pyw-p%)aonf&*ykr^d919)0fv#)%y%7f^f3(k!k_)^h1snh%_g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'passageway',
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

ROOT_URLCONF = 'datapassageway.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'datapassageway.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',   # os.environ.get('DJANGO_MYSQL_USER')
        'PASSWORD':  '',  # os.environ.get('DJANGO_MYSQL_PASSWORD'),
        'HOST': '',  # os.environ.get('DJANGO_MYSQL_HOST'),
        'PORT': 3306,
        # 'OPTIONS': {'charset': 'utf8mb4'},
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'datapassageway',
        # 'USER': 'root',   # os.environ.get('DJANGO_MYSQL_USER')
        # 'PASSWORD':  '920125',  # os.environ.get('DJANGO_MYSQL_PASSWORD'),
        # 'HOST': '127.0.0.1',  # os.environ.get('DJANGO_MYSQL_HOST'),
        # 'PORT': 3306,
        # 'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOG_PATH = os.path.join(BASE_DIR, 'log')
if not os.path.isdir(LOG_PATH):
    os.mkdir(LOG_PATH)

LOGGING = {
    # version 值只能为1
    'version': 1,
    # True 表示禁用loggers
    'disable_existing_loggers': False,

    # < 格式化 >
    'formatters': {
        # 可以设置多种格式，根据需要选择保存的格式
        'default': {
            'format': '%(levelname)s %(funcName)s %(module)s %(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(asctime)s %(message)s'
        }
    },

    # < 处理信息 >
    'handlers': {
        'sql_handlers': {
            'level': 'DEBUG',
            # 指定日志文件大小，若超过指定的文件大小，会再生成一个新的日志文件保存日志信息
            'class': 'logging.handlers.RotatingFileHandler',
            # 指定文件大小
            # 1M=1024kb 1kb=1024b
            'maxBytes': 5 * 1024 * 1024,
            # 文件地址
            'filename': '%s/sql_log.txt' % LOG_PATH,
            # 指定保存格式
            'formatter': 'default'
        },
    },

    'loggers': {
        'sql': {
            'handlers': ['sql_handlers'],
            'level': 'INFO'
        },
    },

    'filters': {

    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'