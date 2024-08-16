"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
{% if cookiecutter.development_mode != "template" %}
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
{% endif %}


urlpatterns = [
    path("admin/", admin.site.urls),
{% if cookiecutter.use_ckeditor == "y" %}
    path("ckeditor/", include("django_ckeditor_5.urls")),
{% endif %}
    # Template urls
    path("sample/", include(("apps.sample.urls", "sample"))),
    # API urls
{% if cookiecutter.development_mode == "api" %}
    path("", include(("apps.api.urls", "api"))),
    # API document
    path(
        "download/",
        SpectacularAPIView.as_view(api_version="v1"),
        name="schema",
    ),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
{% elif cookiecutter.development_mode == "both" %}
    path("api/", include(("apps.api.urls", "api"))),
    # API document
    path(
        "api/schema/download/",
        SpectacularAPIView.as_view(api_version="v1"),
        name="schema",
    ),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
{% endif %}

] 

{% if cookiecutter.use_cloud_storage != "y" %}
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
{% endif %}
