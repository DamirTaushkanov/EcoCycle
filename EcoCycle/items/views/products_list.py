from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from items.models import Products
from ..serializers.serializers import ProductSerializer

@api_view(['GET'])
def products_list(request):
    if request.method == 'GET':
        data = Products.objects.filter(user=request.user)
        products_list = ProductSerializer(data, many=True)
        return Response(products_list.data)