from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Delivery, Client, Message


class DeliveryViewSetTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = APIClient()
        self.delivery = Delivery.objects.create(message='Test Message')

    def test_list_deliveries(self):
        url = reverse('delivery-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Assuming only one delivery is created

    def test_create_delivery(self):
        url = reverse('delivery-list')
        data = {'message': 'New Delivery'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Delivery.objects.count(), 2)  # Assuming one delivery already exists

    def test_get_general_statistic(self):
        url = reverse('delivery-get-general-statistic')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total deliveries'], 1)  # Assuming one delivery is created
        self.assertEqual(response.data['total messages'], 0)  # Assuming no messages are created

    def test_get_detailed_statistic(self):
        url = reverse('delivery-get-detailed-statistic', args=[self.delivery.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['delivery id'], self.delivery.id)
        self.assertEqual(response.data['total messages in the delivery'], 0)  # Assuming no messages are created


class ClientViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client_1 = Client.objects.create(tel='71234567890', code='123')

    def test_list_clients(self):
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Assuming only one client is created

    def test_create_client(self):
        url = reverse('client-list')
        data = {'tel': '71234567891', 'code': '456'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 2)  # Assuming one client already exists


class MessageViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.delivery = Delivery.objects.create(message='Test Message')
        self.client_1 = Client.objects.create(tel='71234567890', code='123')

    def test_list_messages(self):
        url = reverse('message-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)  # Assuming no messages are created

    def test_create_message(self):
        url = reverse('message-list')
        data = {'delivery': self.delivery.id, 'client': self.client_1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)  # Assuming one message is created
