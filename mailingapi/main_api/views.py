from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DeliverySerializer, ClientSerializer, MessageSerializer
from .models import Delivery, Message, Client
from rest_framework import generics, viewsets, decorators
from .utils import make_log



class ClientsViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        make_log(1, 'Client')
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        client_id = kwargs.get('pk')
        make_log(2, 'Client', id=client_id)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        client_id = kwargs.get('pk')
        make_log(3, 'Client', id=client_id)
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        make_log(4, 'Client')
        return super().list(request, *args, **kwargs)


class DeliveryViewSet(viewsets.ModelViewSet):

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

    def create(self, request, *args, **kwargs):
        make_log(1, 'Delivery')
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        del_id = kwargs.get('pk')
        make_log(2, 'Delivery', id=del_id)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        del_id = kwargs.get('pk')
        make_log(3, 'Delivery', id=del_id)
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        make_log(4, 'Delivery')
        return super().list(request, *args, **kwargs)

    @decorators.action(detail=False, methods=['get'])
    def get_general_statistic(self, request):
        make_log(0, "Retrieving general statistics.")
        total_deliveries = Delivery.objects.count()
        total_messages = Message.objects.count()
        messages_sent = Message.objects.filter(sending_status='sent').count()
        response = {
            'total deliveries': total_deliveries,
            'total messages': total_messages,
            'messages sent': messages_sent
        }
        return Response(response)

    @decorators.action(detail=True, methods=['get'])
    def get_detailed_statistic(self, request, pk):
        make_log(0, f"Retrieving detailed statistics for Delivery ID: {pk}.")
        delivery = Delivery.objects.get(id=pk)
        messages = Message.objects.filter(delivery=delivery).count()
        messages_sent = Message.objects.filter(delivery=delivery, sending_status='sent').count()
        response = {
            'delivery id': delivery.id,
            'total messages in the delivery': messages,
            'messages sent': messages_sent
        }
        return Response(response)



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        make_log(1, 'Message')
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        del_id = kwargs.get('pk')
        make_log(2, 'Message', id=del_id)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        del_id = kwargs.get('pk')
        make_log(3, 'Message', id=del_id)
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        make_log(4, 'Message')
        return super().list(request, *args, **kwargs)



