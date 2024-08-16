import os


{% if cookiecutter.email_backend == 'gmail' %}
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")
{% elif cookiecutter.email_backend == 'console' %}
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
{% endif %}
