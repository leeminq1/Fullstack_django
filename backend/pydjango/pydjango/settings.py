# settings.py

from pathlib import Path
from pymongo import MongoClient
from decouple import config

# MongoDB 설정
MONGO_URI = config("MONGO_URI")

# Secret Key
SECRET_KEY = config("SECRET_KEY")

# Debug 설정
DEBUG = config("DEBUG", default=True, cast=bool)

BASE_DIR = Path(__file__).resolve().parent.parent

# MongoDB 연결 설정
client = MongoClient(MONGO_URI)
db = client.get_database()  # 기본 데이터베이스로 연결

# CORS 설정
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8081",  # 허용할 도메인
    "http://localhost:8081",  # 허용할 도메인
]

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pydjango.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.dummy",  # MongoDB는 Django ORM을 사용하지 않으므로 dummy 엔진 사용
        "NAME": "local",  # 사용할 MongoDB 데이터베이스 이름
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 템플릿 파일 경로
        'APP_DIRS': True,  # 앱의 템플릿을 자동으로 로드
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


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
