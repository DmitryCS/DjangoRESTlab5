from rest_framework import serializers
from Messages.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'playerFrom', 'playerTo', 'messageText')