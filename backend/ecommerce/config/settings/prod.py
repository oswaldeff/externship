from .base import *


# def read_secret(secret_name):
# 	file = open('/run/secrets/' + secret_name)
# 	secret = file.read()
# 	secret = secret.rstrip().lstrip()
# 	file.close()
# 	return secret


# os.environ.setdefault('DJANGO_SECRET_KEY', read_secret('DJANGO_SECRET_KEY'))
# os.environ.setdefault('DATABASES_HOST', read_secret('DATABASES_HOST'))
# os.environ.setdefault('DATABASES_NAME', read_secret('DATABASES_NAME'))
# os.environ.setdefault('DATABASES_USER', read_secret('DATABASES_USER'))
# os.environ.setdefault('DATABASES_PASSWORD', read_secret('DATABASES_PASSWORD'))
# os.environ.setdefault('DATABASES_PORT', read_secret('DATABASES_PORT'))
# os.environ.setdefault('ALGORITHM', read_secret('ALGORITHM'))
# os.environ.setdefault('KAKAO_CLIENT_ID', read_secret('KAKAO_CLIENT_ID'))
# os.environ.setdefault('PHONE_NUMBER', read_secret('PHONE_NUMBER'))
# os.environ.setdefault('AWS_ACCESS_KEY_ID', read_secret('AWS_ACCESS_KEY_ID'))
# os.environ.setdefault('AWS_SECRET_ACCESS_KEY', read_secret('AWS_SECRET_ACCESS_KEY'))
# os.environ.setdefault('AWS_S3_ADDRESS', read_secret('AWS_S3_ADDRESS'))
# os.environ.setdefault('AWS_REGION', read_secret('AWS_REGION'))
# os.environ.setdefault('AWS_S3_HOST', read_secret('AWS_S3_HOST'))
# os.environ.setdefault('AWS_BUCKET_NAME', read_secret('AWS_BUCKET_NAME'))


# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
# SIMPLE_JWT['SIGNING_KEY'] = os.environ.get('DJANGO_SECRET_KEY')
# DATABASES['default']['HOST'] = os.environ.get('DATABASES_HOST')
# DATABASES['default']['NAME'] = os.environ.get('DATABASES_NAME')
# DATABASES['default']['USER'] = os.environ.get('DATABASES_USER')
# DATABASES['default']['PASSWORD'] = os.environ.get('DATABASES_PASSWORD')
# DATABASES['default']['PORT'] = os.environ.get('DATABASES_PORT')
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_S3_ADDRESS = os.environ.get('AWS_S3_ADDRESS')
# AWS_REGION = os.environ.get('AWS_REGION')
# AWS_S3_HOST = os.environ.get('AWS_S3_HOST')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')