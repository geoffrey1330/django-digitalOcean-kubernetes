import os

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME='django-k8s-stat'
AWS_S3_ENDPOINT_URL="https://django-k8s-stat.nyc3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION="https://django-k8s-stat.nyc3.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "myproj.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = 'myproj.cdn.backends.StaticRootS3BotoStorage'