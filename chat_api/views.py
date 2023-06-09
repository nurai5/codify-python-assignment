from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer, MessageListSerializer
from .utils import complete_prompt


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.validated_data['prompt_message']
        response = complete_prompt(message)
        serializer.save(message=message, response=response)


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
