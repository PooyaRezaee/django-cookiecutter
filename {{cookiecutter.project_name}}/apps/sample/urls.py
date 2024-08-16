from django.urls import path
from .views import SampleView


urlpatterns = [
    path('',SampleView.as_view(), name="hello"),
]