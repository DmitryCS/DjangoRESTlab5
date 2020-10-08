from rest_framework import serializers
from GameMap.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'locationId', 'description','locationType')