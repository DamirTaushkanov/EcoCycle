from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers.profile_serializer import ProfileCreateSerializer


@api_view(['POST'])
def set_profile(request):
    profile = ProfileCreateSerializer(data=request.data, context={'request': request})
    if profile.is_valid():
        profile.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(profile.errors, status=status.HTTP_400_BAD_REQUEST)