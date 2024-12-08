from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Users

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password')

    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        return user