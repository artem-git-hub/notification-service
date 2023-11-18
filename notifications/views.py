from django.utils import timezone
from rest_framework import generics

from notifications.utils import send_message
from .models import Client, Dispatch, Message
from .serializers import ClientSerializer, DispatchSerializer, MessageSerializer
from .celery_tasks import send_dispatch_messages


class ClientListCreateView(generics.ListCreateAPIView):
    """
    get:
    Возвращает список всех клиентов.

    post:
    Создает запись клиента
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Возвращает полную информацию о клиенте по id.

    put:
    Полное изменение записи клиента по id.

    patch:
    Изменение некоторых полей записи клиента по id.

    delete:
    Удаление записи клиента.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DispatchListCreateView(generics.ListCreateAPIView):
    """
    get:
    Возвращает список всех рассылок.

    post:
    Создает рассылку
    """
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

    def perform_create(self, serializer):
        """
        Create a new dispatch.
        """
        instance = serializer.save()

        
        if instance.start_datetime > timezone.now():
            delay_seconds = (instance.start_datetime - timezone.now()).total_seconds()
            send_dispatch_messages.apply_async((instance.id,), countdown=delay_seconds)
        else:
            
            send_dispatch_messages.delay(instance.id)

class DispatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Возвращает полную информацию о рассылке по id.

    put:
    Полное изменение рассылки по id.

    patch:
    Изменение некоторых полей по id.

    delete:
    Удаление рассылки.
    """
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    """
    get:
    Возвращает список всех сообщений.

    post:
    Создает сообщение и отправляет его во внешний сервис
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        
        instance = serializer.save()

        
        message_data = {
            "id": instance.id,
            "phone": instance.client.phone_number,
            "text": instance.dispatch.message_text,
        }

        
        response_data = send_message(message_data)

        if response_data:
            instance.status = "success"
        else:
            instance.status = "failed"

        instance.save()

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Возвращает полную информацию о сообщении по id.

    put:
    Полное изменение сообщения по id.

    patch:
    Изменение некоторых полей по id.

    delete:
    Удаление сообщения.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

