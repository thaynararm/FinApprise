

from pathlib import Path, os
from dotenv import load_dotenv
from decouple import config
from django.conf.global_settings import DATE_FORMAT, DATE_INPUT_FORMATS
import logging

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Configura o nível de log como DEBUG durante o desenvolvimento
    },
}

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users.apps.UsersConfig',
    'apps.clients.apps.ClientsConfig',
    'apps.index.apps.IndexConfig',
    'apps.suppliers.apps.SuppliersConfig',
    'apps.utilities.apps.UtilitiesConfig',
    'apps.revenues.apps.RevenuesConfig',
    # 'apps.expenses.apps.ExpensesConfig',
    # 'apps.products.apps.ProductsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
]


ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'NewFinApprise',
        'USER': 'SA',
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': 'localhost',  
        'PORT': '',  
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'



USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static'),
    os.path.join(BASE_DIR, 'apps/index/static'),
    os.path.join(BASE_DIR, 'apps/users/static'),
    os.path.join(BASE_DIR, 'apps/revenues/static'),
    # os.path.join(BASE_DIR, 'apps/expenses/static'),
    # os.path.join(BASE_DIR, 'apps/products/static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media

MEDIA_ROOT = [
    os.path.join(BASE_DIR, 'media'),
]

MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# messages

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success'
}

# Separador de números decimais
DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True

DATE_FORMAT = ['%d/%m/%Y',]

DATE_INPUT_FORMATS = ['%d/%m/%Y',]