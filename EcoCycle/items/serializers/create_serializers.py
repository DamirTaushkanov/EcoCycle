from rest_framework import serializers
from items.models import Products, ProductImages
from accounts.models import Users


class ProductCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True
    )
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), write_only=True, required=False)

    class Meta:
        model = Products
        fields = ('user', 'title', 'count', 'categories', 'description', 'trade', 'images')

    def create(self, validated_data):
        user = self.context['request'].user
        images_data = validated_data.pop('images', [])
        product = Products.objects.create(user=user, **validated_data)
        for image_data in images_data:
            ProductImages.objects.create(product=product, images=image_data)
        return product