from rest_framework import serializers

from chat.models import Message
from items.models import Products, ProductImages
from accounts.models import Users


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('receiver', 'content')
