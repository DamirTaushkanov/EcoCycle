from rest_framework import serializers
from chat.models import Message
from accounts.models import Users
from items.models import Products


class MessageCreateSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(),
        write_only=True,
        required=False
    )
    sender_product = serializers.PrimaryKeyRelatedField(
        queryset=Products.objects.all(),
        required=False,
        allow_null=True
    )
    receiver_product = serializers.PrimaryKeyRelatedField(
        queryset=Products.objects.all(),
        required=False,
        allow_null=True
    )
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content', 'sender_product', 'receiver_product']

    def create(self, validated_data):
        sender = self.context['request'].user
        sender_product = validated_data.pop('sender_product', None)
        receiver_product = validated_data.pop('receiver_product', None)
        message = Message.objects.create(
            sender=sender,
            sender_product=sender_product,
            receiver_product=receiver_product,
            **validated_data
        )
        return message