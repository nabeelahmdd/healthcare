from custom.serializers import (
    UserSerializer, UserSerializerWithToken,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import mixins, viewsets
from custom.models import User


# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.filter(soft_delete=False)
    serializer_class = UserSerializer
