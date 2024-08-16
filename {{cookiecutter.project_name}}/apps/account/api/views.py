from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from drf_spectacular.utils import extend_schema

from core import logger
{% if cookiecutter.development_mode != "api" %}
from ..models import User
from ..services.user import create_user
from ..validators import validate_password
{% else %}
from .models import User
from .services.user import create_user
from .validators import validate_password
{% endif %}


class RegisterAPIView(APIView):
    class InputRegisterSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=256)
        password = serializers.CharField(
            validators=[validate_password]
        )

    class OutPutRegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ("email", "joined_at")

    @extend_schema(
        request=InputRegisterSerializer,
        responses={200: OutPutRegisterSerializer},
    )
    def post(self, request):
        srz = self.InputRegisterSerializer(data=request.data)
        srz.is_valid(raise_exception=True)

        try:
            email = srz.data["email"]
            password = srz.data["password"]
            user = create_user(email, password)
            return Response(
                self.OutPutRegisterSerializer(
                    user,
                ).data
            )
        except Exception as e:
            logger.error(f"Error in register user {e}")
            return Response(
                {"detail": "Internal Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
