from .base import *


ALLOWED_HOSTS += [
    os.environ.get('AWS_PUBLIC_DNS'),
]