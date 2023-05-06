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
    specialty = serializers.CharField(
        max_length=250, required=False, write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'password', 'phone_number',
            'category', 'specialty'
        ]
        extra_kwargs = {
            'specialty': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        specialty_data = validated_data.pop('specialty', None)

        if validated_data.get('category') == 'd' and specialty_data is None:
            raise serializers.ValidationError(
                "Specialty is required for doctors")
        user = User(**validated_data)
        user.is_active = False
        user.set_password(validated_data['password'])
        user.save()

        if user.category == 'd' and specialty_data is not None:
            doctor = Doctor.objects.create(
                user=user, specialty=specialty_data, cr_by=user, up_by=user)
            doctor.save()

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
