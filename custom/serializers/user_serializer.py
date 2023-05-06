from rest_framework import serializers
from custom.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from base.models import Doctor


class UserSerializer(serializers.ModelSerializer):
    CATEGORY_CHOICES = (
        ('d', 'Doctor'),
        ('p', 'Patient'),
        ('r', 'Receptionist'),
    )
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'password', 'phone_number',
            'category'
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


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'image', 'token', 'category'
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get_category(self, obj):
        return obj.get_category_display()
