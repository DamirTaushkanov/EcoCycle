from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from items.models import Products

from items.serializers.create_serializers import ProductCreateSerializer


@api_view(['POST'])
def create_product(request):
    product = ProductCreateSerializer(data=request.data, context={'request': request})
    if product.is_valid():
        product.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request):
    try:
        product = Products.objects.get(id=request.data.get('product'))
    except Products.DoesNotExist:
        return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

