from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'login', 'email', 'first_name', 'last_name', 'date_joined', 'last_login']
