from pathlib import Path
import dj_database_url
import os
import urllib.parse
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')  # Usar una variable de entorno para mayor seguridad

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Cambiar a False para producción

ALLOWED_HOSTS = [
    '*',
    '192.168.10.19',
    'myproyecto-m9gh.onrender.com',
    'riotur.co',
    'www.riotur.co',
]
CORS_ALLOW_ALL_ORIGINS = True

#CORS_ALLOWED_ORIGINS = [
#    "https://localhost:4200",  # Para desarrollo en Angular
#    "https://192.168.10.19",
#    "https://riotur.co",      # Para el dominio de producción
#    "https://www.riotur.co",  # Para el subdominio de producción
#    "https://myproyecto-m9gh.onrender.com",  # El dominio de la API en Render
#]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'myproyecto.urls'

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

WSGI_APPLICATION = 'myproyecto.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bbxys4ynowhep7txyemp',
        'USER': 'uifdezz7yx3fztbg',
        'PASSWORD': 'Xkh16tRUUsNerNM1Lcj',
        'HOST': 'bbxys4ynowhep7txyemp-mysql.services.clever-cloud.com',
        'PORT': '21649'
    }
}



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
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# Configura la ruta para archivos estáticos en producción (por ejemplo, en Render, puedes configurar un almacenamiento de archivos estáticos adecuado).
STATIC_URL = '/static/'

# Configura la ruta de los archivos estáticos para producción, por ejemplo, en un bucket de S3 o en Render.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

# Seguridad adicional para producción
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600  # 1 hora de seguridad HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True