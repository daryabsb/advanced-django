# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.
from src.settings.components.env import config
import dj_database_url

DATABASE_URL = config("B1_DATABASE_URL", default=None)
HOST_ENV = config('HOST_ENV', default='office')

# if DATABASE_URL is None or HOST_ENV == 'office':
#     DATABASE_URL = "postgres://postgres:postgres2019@172.16.10.6/aronneon"
# else:
#     DATABASE_URL = "postgres://postgres:postgres2019@188.72.18.2/aronneon"

if DATABASE_URL is not None:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True
        )
    }
else:
    DATABASE_NAME = config("DATABASE_NAME", default='aronneon')
    DATABASE_USER = config("DATABASE_USER", default='postgres')
    DATABASE_PASSWORD = config("DATABASE_PASSWORD", default='postgres')
    DATABASE_HOST = config("DATABASE_HOST", default='127.0.0.1')
    DATABASE_PORT = config("DATABASE_PORT", default=5432)

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
            'HOST': DATABASE_HOST,
            'PORT': DATABASE_PORT,
        }
    }
