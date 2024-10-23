"""
Django settings for chatproject project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# from pathlib import Path
# from datetime import timedelta
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-resm%*0$1=od7)#z1^0jw$4rkz_5!re0joh^e2ej%yssesom9a'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
#
# # Application definition
#
# INSTALLED_APPS = [
#     'daphne',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'channels',
#     'chat_app',
#     'rest_framework',
#     'corsheaders',
#     'auth_app',
#     'crud_app',
# ]
#
# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'chatproject.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# # Daphne for ASGI
# ASGI_APPLICATION = 'chatproject.asgi.application'
#
# # Redis Channel Layer for WebSockets
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('localhost', 6379)],
#         },
#     },
# }
#
# # SimpleJWT settings for token expiration
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(hours=12),  # Access token valid for 12 hours
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=30),  # Refresh token valid for 30 days
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'AUTH_HEADER_TYPES': ('Bearer',),
# }
#
# # REST Framework settings with JWT Authentication
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
# }
#
# # Database: Connect to MongoDB without environment variables
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'chat_db',
#         'CLIENT': {
#             'host': 'localhost',
#             'port': 27017,
#             'serverSelectionTimeoutMS': 60000,  # Optional: Increase the timeout for connection retries
#         }
#     }
# }
#
# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True
#
# # Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
#
# # Default primary key field type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
#
#






import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-resm%*0$1=od7)#z1^0jw$4rkz_5!re0joh^e2ej%yssesom9a')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(',')


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'chat_app',
    'rest_framework',
    'corsheaders',
    'auth_app',
    'crud_app',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chatproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Daphne for ASGI
ASGI_APPLICATION = 'chatproject.asgi.application'

# Redis Channel Layer for WebSockets
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [(os.getenv('REDIS_HOST', 'redis'), int(os.getenv('REDIS_PORT', 6379)))],
#         },
#     },
# }

# Default Redis host and port
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

# Check if running in Kubernetes
if 'KUBERNETES_SERVICE_HOST' in os.environ:
    redis_host = os.getenv('REDIS_HOST', 'redis-service.my-chat-app.svc.cluster.local')

# # Channel layers configuration
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [(redis_host, redis_port)],
#             "capacity": 1000,  # Adjust based on your needs
#             "expiry": 10,  # Optional: Message expiry time in seconds
#         },
#     },
# }


# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [
#                 ("redis-0.redis-headless.my-chat-app.svc.cluster.local", 6379),
#                 ("redis-1.redis-headless.my-chat-app.svc.cluster.local", 6379),
#                 ("redis-2.redis-headless.my-chat-app.svc.cluster.local", 6379),
#             ],
#             "capacity": 1000,
#             "expiry": 10,
#         },
#     },
# }

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [
                ("redis-sentinel.my-chat-app.svc.cluster.local", 26379)
            ],
            "service_name": "mymaster",  # Name of the Redis master configured in Sentinel
            "sentinel": True,  # Enable Sentinel mode
            "capacity": 1000,
            "expiry": 10,
        },
    },
}

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [{
#                 'sentinel': True,
#                 'sentinel_hosts': [
#                     ('redis-sentinel.my-chat-app.svc.cluster.local', 26379),
#                 ],
#                 'service_name': 'mymaster',
#                 'password': None,  # Add if you have password configured
#                 'db': 0,
#                 'prefix': '',  # Add a prefix if needed
#             }],
#             'capacity': 1000,
#             'expiry': 10,
#         },
#     },
# }

# SimpleJWT settings for token expiration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=12),  # Access token valid for 12 hours
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),  # Refresh token valid for 30 days
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# REST Framework settings with JWT Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Database: Connect to MongoDB using environment variables

MONGO_HOSTS = os.getenv('MONGO_HOSTS')  # For Kubernetes replica set hosts
MONGO_HOST = os.getenv('MONGO_HOST', 'mongo')  # For Docker (single host)
MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'chat_db')
MONGO_REPLICA_SET = os.getenv('MONGO_REPLICA_SET')  # Optional: Only for replica sets

if MONGO_HOSTS:  # Use replica set configuration if available
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': MONGO_DB_NAME,
            'CLIENT': {
                'host': MONGO_HOSTS.split(','),
                'port': MONGO_PORT,
                'replicaSet': MONGO_REPLICA_SET,
                'retryWrites': True,
                'serverSelectionTimeoutMS': 60000,
                'readPreference': 'primaryPreferred',
            }
        }
    }
else:  # Fallback to single MongoDB instance configuration (for Docker)
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': MONGO_DB_NAME,
            'CLIENT': {
                'host': MONGO_HOST,
                'port': MONGO_PORT,
                'serverSelectionTimeoutMS': 60000,
            }
        }
    }


# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': os.getenv('MONGO_DB_NAME', 'chat_db'),
#         'CLIENT': {
#             'host': os.getenv('MONGO_HOST', 'mongo'),
#             'port': int(os.getenv('MONGO_PORT', 27017)),
#             'serverSelectionTimeoutMS': 60000,  # Optional: Increase the timeout for connection retries
#         }
#     }
#}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
