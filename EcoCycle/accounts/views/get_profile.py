from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from accounts.models import Profile
from ..serializers.profile_serializer import ProfileSerializer

@api_view(['GET'])
def get_profile(request):
    try:
        data = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Response({'detail': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    profile = ProfileSerializer(data)
    return Response(profile.data)