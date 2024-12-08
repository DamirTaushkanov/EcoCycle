from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers.locate_serializer import LocateCreateSerializer

@api_view(['POST'])
def set_locate(request):
    locate = LocateCreateSerializer(data=request.data, context={'request': request})
    if locate.is_valid():
        locate.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(locate.errors, status=status.HTTP_400_BAD_REQUEST)
