from .base import *
from pathlib import Path

DEBUG = False

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']
else:
    import string
    from random import choice
    chars = string.ascii_letters + string.digits
    SECRET_KEY = "".join(choice(chars) for x in range(50))

ALLOWED_HOSTS = ['*'] 
p = Path('/') / 'srv'

STATIC_ROOT = p / 'static'
MEDIA_ROOT = p / 'media'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
try:
    from .local import *
except ImportError:
    pass
