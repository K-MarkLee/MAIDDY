from pathlib import Path
from decouple import config 
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("DJANGO_SECRET_KEY", "fallback_secret_key")

DEBUG = False
FRONTEND_IP = config("FRONTEND_IP")
BACKEND_IP = config("BACKEND_IP")

ALLOWED_HOSTS = [
    "maiddy.co.kr",
    FRONTEND_IP,       
    BACKEND_IP, 
    "maiddy.co.kr:3000",
    "maiddy_ai:5001",
    "api.maiddy.co.kr"
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://maiddy.co.kr",   
    f"http://{FRONTEND_IP}",  
    "http://localhost:3000", 
    f"http://{BACKEND_IP}:8000", 
    "http://maiddy.co.kr:3000",
    "http://maiddy_ai:5001"
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]



INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # my apps
    "users",
    "diaries",
    "todo",
    "schedules",
    
    # thrid party apps
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist", 

    "corsheaders",
]

# 사용자 모델 변경
AUTH_USER_MODEL = 'users.User' 

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 프론트 연결코드 반드시 CommonMiddleware 전에 위치
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "maiddy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = "maiddy.wsgi.application"


#postgresql 설정 (나중에 .env로 변경)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql", # postgresql로 변경
        "NAME": config("DB_NAME"), # 데이터베이스 이름
        "USER": config('DB_USER'), # 데이터베이스 유저
        "PASSWORD": config('DB_PASSWORD'), # 데이터베이스 비밀번호
        "HOST": config('DB_HOST'), # 데이터베이스 호스트
        "PORT": config('DB_PORT'), 
    }
}


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

LANGUAGE_CODE = "en-us" 

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication', 
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1), 
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30), 
    'ROTATE_REFRESH_TOKENS': True, 
    'BLACKLIST_AFTER_ROTATION': True, 
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'