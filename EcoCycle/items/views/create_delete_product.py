from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from items.models import Products

from items.serializers.create_serializers import ProductCreateSerializer


@api_view((['POST']))
@login_required
def create_product(request):
    if request.method == 'POST':
        product = ProductCreateSerializer(data=request.data, context={'request': request})
        print(product)
        if product.is_valid():
            product.save()
            return Response(status=status.HTTP_201_CREATED)
        print(product.errors)  # Печатает ошибки валидации
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@login_required
def delete_product(request, product_id):
    if request.method == 'DELETE':
        try:
            product = Products.objects.get(product_id=product_id)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

