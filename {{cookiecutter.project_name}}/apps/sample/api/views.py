from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from drf_spectacular.utils import extend_schema


class SampleAPIView(APIView):
    """
    Just Sample
    """
    throttle_scope = 'testing'

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=256)
    # class OutPutSerializer(serializers.ModelSerializer):
    #     pass
    
    @extend_schema(
        request=InputSerializer,
        responses={200: {"msg":"say hello"}},
    )
    def post(self, request):
        srz = self.InputSerializer(request.data)
        srz.is_valid(raise_exception=True)
        
        name = srz.data['name']
        
        return Response({"msg":f"Hello {name}"}, status=status.HTTP_200_OK)
    
