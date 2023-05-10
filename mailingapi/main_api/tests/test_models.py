from django.test import TestCase
from django.utils import timezone
from ..models  import Delivery, Client, Message


class DeliveryModelTest(TestCase):
    def test_delivery_creation(self):
        delivery = Delivery.objects.create(message='Test Message')
        self.assertEqual(delivery.message, 'Test Message')
        self.assertIsNotNone(delivery.date_of_creation)
        self.assertIsNotNone(delivery.final_date)
        self.assertEqual(delivery.code, '')
        self.assertEqual(delivery.tag, '')

    def test_delivery_final_date_auto_set(self):
        delivery = Delivery.objects.create(message='Test Message')
        expected_final_date = delivery.date_of_creation + timezone.timedelta(days=1)
        self.assertEqual(delivery.final_date, expected_final_date)


class ClientModelTest(TestCase):
    def test_client_creation(self):
        client = Client.objects.create(tel='71234567890', code='123', tag='Test')
        self.assertEqual(client.tel, '71234567890')
        self.assertEqual(client.code, '123')
        self.assertEqual(client.tag, 'Test')
        self.assertEqual(client.timezone, 'UTC')


class MessageModelTest(TestCase):
    def setUp(self):
        self.delivery = Delivery.objects.create(message='Test Message')
        self.client = Client.objects.create(tel='71234567890', code='123')

    def test_message_creation(self):
        message = Message.objects.create(delivery=self.delivery, client=self.client)
        self.assertEqual(message.delivery, self.delivery)
        self.assertEqual(message.client, self.client)
        self.assertEqual(message.sending_status, 'not sent')


class ModelTestCase(TestCase):
    def setUp(self):
        self.delivery = Delivery.objects.create(message='Test Message')
        self.client = Client.objects.create(tel='71234567890', code='123')
        self.message = Message.objects.create(delivery=self.delivery, client=self.client)

    def test_str_methods(self):
        self.assertEqual(str(self.delivery), f'Delivery {self.delivery.pk}')
        self.assertEqual(str(self.client), f'Client {self.client.pk}')
        self.assertEqual(str(self.message), f'Message {self.message.pk}')
