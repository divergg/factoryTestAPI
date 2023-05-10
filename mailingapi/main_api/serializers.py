from .models import Delivery, Client, Message
from rest_framework.serializers import ModelSerializer


class DeliverySerializer(ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'