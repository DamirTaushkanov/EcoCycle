from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from items.models import Products
from ..serializers.serializers import ProductSerializer

@api_view(['GET'])
def products_list(request):
    try:
        data = Products.objects.filter(user=request.user)
    except Products.DoesNotExist:
        return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    products_list = ProductSerializer(data, many=True)
    return Response(products_list.data)