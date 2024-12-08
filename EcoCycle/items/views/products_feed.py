from django.utils.timezone import now, timedelta

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from items.models import Products
from ..serializers.serializers import ProductSerializer

@api_view(['POST'])
def products_feed(request):
    try:
        # Дата за последние 7 дней
        last_week = now() - timedelta(days=7)
        if request.data.get('category'):
            data = Products.objects.filter(
                categories=request.data.get('category'),
                date_added__gte=last_week
            ).exclude(user=request.user).order_by('-date_added')[:10]
        else:
            data = Products.objects.filter(
                date_added__gte=last_week
            ).exclude(user=request.user).order_by('-date_added')[:10]
        products_feed = ProductSerializer(data, many=True)
        return Response(data=products_feed.data)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)