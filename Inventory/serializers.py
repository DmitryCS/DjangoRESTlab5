from rest_framework import serializers
from Inventory.models import ItemType, Item


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ('id', 'type')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'itemType', 'quality', 'owner')