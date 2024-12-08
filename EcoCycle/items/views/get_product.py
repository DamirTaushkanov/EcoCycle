from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from items.models import Products
from ..serializers.serializers import ProductSerializer

@api_view(['GET'])
def get_product(request):
    try:
        data = Products.objects.get(id=request.data.get('product'))
    except Products.DoesNotExist:
        return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    product = ProductSerializer(data)
    return Response(product.data)