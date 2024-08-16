from django.urls import path
from .views import SampleAPIView


urlpatterns = [
    path("hello/", SampleAPIView.as_view(), name="hello"),
]
