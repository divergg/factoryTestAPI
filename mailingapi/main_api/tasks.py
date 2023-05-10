import os
import requests
from celery import shared_task
from dotenv import load_dotenv
from .models import Delivery, Client, Message
import json
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)
log_file = 'celery.log'
file_handler = logging.FileHandler(log_file)
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

@shared_task(bind=True)
def send_message(self, client_id, delivery_id, message_id):
    load_dotenv()
    client = Client.objects.get(id=client_id)
    delivery = Delivery.objects.get(id=delivery_id)
    message = Message.objects.get(id=message_id)
    URL = os.getenv("URL") + f'{message.id}'
    TOKEN = os.getenv("TOKEN")
    headers = {
        'authorization': f'Bearer {TOKEN}',
        'content-type': 'application / json'
    }

    payload = {
        'id': message.pk,
        'phone': client.tel,
        'text': delivery.message
    }
    current_time = timezone.now()

    if delivery.date_of_creation <= current_time <= delivery.final_date:
        try:
            req = requests.post(URL, headers=headers, json=payload)
            print(json.loads(req.text))
            logger.info(f'The message #{message.id} has been sent')
            message.sending_status = 'sent'
            message.save()
        except:
            logger.error(f'An error occured during sending of the message #{message.id}')
            error = json.loads(req.text)
            logger.error(f'The external server returned: {error}. Retry in 5 min')
            raise self.retry(countdown=300)
    else:
        raise self.retry(countdown=1800)








