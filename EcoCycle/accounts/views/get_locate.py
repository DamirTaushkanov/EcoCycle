from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from accounts.models import Locate
from ..serializers.locate_serializer import LocateSerializer

@api_view(['GET'])
def get_locate(request):
    try:
        data = Locate.objects.get(user=request.user)
    except Locate.DoesNotExist:
        return Response({'detail': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    locate = LocateSerializer(data)
    return Response(locate.data)