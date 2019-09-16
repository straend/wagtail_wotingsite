from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%ud$h7q4+x()3i3+l-@5336ji3vfjf6yuj9prwc6-=ce$&i691'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'dev', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'dev', 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'dev', 'dev_db.sqlite3'),
    }
}

try:
    from .local import *
except ImportError:
    pass
