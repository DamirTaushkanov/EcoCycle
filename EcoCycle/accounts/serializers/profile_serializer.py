from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Profile, Users


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'profile_pic', 'bio')

class ProfileCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), write_only=True, required=False)

    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name',  'profile_pic', 'bio')

    def create(self, validated_data):
        user = self.context['request'].user
        profile_pic = validated_data.pop('profile_pic', None)
        profile = Profile.objects.create(user=user, **validated_data)
        if profile_pic:
            profile.profile_pic = profile_pic
            profile.save()
        return profile