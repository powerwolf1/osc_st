import os
from oscar.defaults import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sfcgt$ef(5*lx8=zms$ysi=5lsuxryec*0*=5-)m33bb7y^a3)'

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

    'django.contrib.sites',
    'django.contrib.flatpages',

    'oscar',
    'oscar.apps.analytics',
    'oscar.apps.checkout',
    'oscar.apps.address',
    'oscar.apps.shipping',
    'oscar.apps.catalogue.reviews',
    'apps.partner.apps.PartnerConfig',
    'oscar.apps.basket',
    'oscar.apps.payment',
    'oscar.apps.offer',
    'apps.order.apps.OrderConfig',
    'oscar.apps.customer',
    'oscar.apps.search',
    'oscar.apps.voucher',
    'oscar.apps.wishlists',
    'apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports',
    'oscar.apps.dashboard.users',
    'oscar.apps.dashboard.orders',
    'apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers',
    'oscar.apps.dashboard.partners',
    'oscar.apps.dashboard.pages',
    'oscar.apps.dashboard.ranges',
    'oscar.apps.dashboard.reviews',
    'oscar.apps.dashboard.vouchers',
    'oscar.apps.dashboard.communications',
    'oscar.apps.dashboard.shipping',
    'apps.catalogue.apps.CatalogueConfig',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'easy_thumbnails',
    'django_tables2',
    'paypal',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'digital_store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'digital_store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DIGITAL_PRODUCT_FILES_ROOT = os.path.join(BASE_DIR, 'digital_products_files')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

OSCAR_THUMBNAILER = 'oscar.core.thumbnails.EasyThumbnails'

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

OSCAR_ORDER_PENDING_STATUS = 'Pending'
OSCAR_ORDER_PAID_STATUS = 'Paid'
OSCAR_ORDER_SHIPPED_STATUS = 'Shipped'
OSCAR_ORDER_REJECTED_STATUS = 'Rejected'

OSCAR_INITIAL_ORDER_STATUS = OSCAR_ORDER_PENDING_STATUS
OSCAR_INITIAL_LINE_STATUS = OSCAR_ORDER_PENDING_STATUS

OSCAR_ORDER_STATUS_PIPELINE = {
    OSCAR_ORDER_PENDING_STATUS: (OSCAR_ORDER_PAID_STATUS, OSCAR_ORDER_REJECTED_STATUS),
    OSCAR_ORDER_PAID_STATUS: (OSCAR_ORDER_SHIPPED_STATUS, OSCAR_ORDER_REJECTED_STATUS),
    OSCAR_ORDER_SHIPPED_STATUS: (),
    OSCAR_ORDER_REJECTED_STATUS: (),
}

OSCAR_DEFAULT_CURRENCY = 'EUR'

OSCAR_MAX_ORDER_DOWNLOAD_ATTEMPTS = 5

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'zaporojan40@gmail.com'
EMAIL_HOST_PASSWORD = '22907AAA'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
