from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Users, Locate

class LocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locate
        fields = ('user', 'latitude', 'longitude', 'timestamp')

class LocateCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), write_only=True, required=False)

    class Meta:
        model = Locate
        fields = ('user', 'latitude', 'longitude', 'timestamp')
    def create(self, validated_data):
        user = self.context['request'].user
        locate = Locate.objects.create(user=user, **validated_data)
        return locate

