from rest_framework import serializers
from custom.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isSuperUser = serializers.SerializerMethodField(read_only=True)
    isManager = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'isAdmin', 'first_name', 'last_name', 'password',
            'isSuperUser', 'isManager', 'phone_number', 'category'
        ]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        user.is_active = False
        user.set_password(validated_data['password'])
        user.save()

        return user

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_isSuperUser(self, obj):
        return obj.is_superuser

    def get_isManager(self, obj):
        return obj.manager


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'isAdmin', 'image', 'token',
            'isSuperUser', 'isManager'
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
