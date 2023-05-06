from rest_framework import serializers
from custom.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from base.models import Doctor


class UserSerializer(serializers.ModelSerializer):
    CATEGORY_CHOICES = (
        ('d', 'Doctor'),
        ('p', 'Patient'),
    )
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'password', 'phone_number',
            'category', 'image', 'gender', 'date_of_birth', 'clinic'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view = self.context.get('view')

        if 'view' in self.context and self.context['view'].action == 'create':
            # Exclude fields for create view
            self.fields.pop('image')
            self.fields.pop('gender')
            self.fields.pop('date_of_birth')
            self.fields.pop('clinic')

        if 'view' in self.context and self.context['view'].action == 'update':
            # Exclude fields for update view
            self.fields.pop('category')
            self.fields.pop('clinic')

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
