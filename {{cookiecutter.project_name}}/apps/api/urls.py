from django.urls import path, include


urlpatterns = [
    path("account/", include(("apps.account{% if cookiecutter.development_mode != 'api' %}.api{% endif %}.urls", "account"))),
    path("sample/", include(("apps.sample{% if cookiecutter.development_mode != 'api' %}.api{% endif %}.urls", "sample"))),
]
