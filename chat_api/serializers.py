from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'prompt_message', 'created_at']


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'prompt_message', 'response', 'created_at']
