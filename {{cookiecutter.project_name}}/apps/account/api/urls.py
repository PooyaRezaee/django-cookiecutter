from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import RegisterAPIView


urlpatterns = [
    path(
        "jwt/",
        include(
            (
                [
                    path("login/", TokenObtainPairView.as_view(), name="login"),
                    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
                    path("verify/", TokenVerifyView.as_view(), name="verify"),
                ],
                "jwt",
            )
        ),
    ),
    path("register/", RegisterAPIView.as_view(), name="register"),
]
