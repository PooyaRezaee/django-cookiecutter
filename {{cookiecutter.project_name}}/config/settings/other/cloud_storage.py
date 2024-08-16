import os

# liara storages
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
AWS_S3_ENDPOINT_URL = 'https://storage.iran.liara.space'
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_SERVICE_NAME = 's3'

# static serving
# STATIC_URL = f"storage.iran.liara.space/{AWS_STORAGE_BUCKET_NAME}/"
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'