from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("User is inactive")
        attrs['user'] = user
        return attrs
class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = CustomUser._meta.get_all_field_names()
