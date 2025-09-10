# LibraryProject/settings.py
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "replace-this-with-a-secure-secret")
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local apps
    "bookshelf",
    "relationship_app",
    "accounts",
    "csp" , 

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # HTTP Strict Transport Security will be set by SecurityMiddleware if configured
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF protection
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # X-Frame-Options header
    "LibraryProject.middleware.ContentSecurityPolicyMiddleware",  # custom CSP header
]

ROOT_URLCONF = "LibraryProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "LibraryProject.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation, strong validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 9}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Localization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static / Media
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Security headers and cookie settings
# In production, DEBUG must be False and these should be True
SECURE_BROWSER_XSS_FILTER = True  # sets X-XSS-Protection header
X_FRAME_OPTIONS = "DENY"  # prevents clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # sets X-Content-Type-Options
# The following should be True in production when running under HTTPS only
SESSION_COOKIE_SECURE = False  # set to True in production with HTTPS
CSRF_COOKIE_SECURE = False     # set to True in production with HTTPS

# HSTS, enable in production under HTTPS
SECURE_HSTS_SECONDS = 0  # set to 31536000 in production
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Use custom user model if you have one, otherwise remove or set correctly
# AUTH_USER_MODEL = "accounts.CustomUser"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Content Security Policy defaults, tuned for your app.
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)  # add external sources explicitly if needed
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")  # avoid 'unsafe-inline' where possible
CSP_IMG_SRC = ("'self'", "data:")
CSP_CONNECT_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")  # example

# Note: You can also install django-csp and configure CSP via settings if you prefer.

