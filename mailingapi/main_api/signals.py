from .tasks import send_message
from django.dispatch import receiver
from .models import Delivery, Client, Message
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q


@receiver(post_save, sender=Delivery, dispatch_uid='handle_new_deivery')
def handle_new_delivery(sender, instance, created, **kwargs):
    """
    Signal, that is activated when new delivery is created
    Sends new requests to testing API
    """
    if created:
        delivery_id = instance.id
        delivery = Delivery.objects.get(id=delivery_id)
        code = delivery.code
        tag = delivery.tag
        clients = Client.objects.filter(Q(code=code)|Q(tag=tag))
        for client in clients:
            message = Message.objects.create(
                send_date=delivery.date_of_creation,
                delivery=delivery,
                client=client
            )
            send_message.apply_async((client.id, delivery.id, message.id),
                                     eta=delivery.date_of_creation,
                                     expires=delivery.final_date)
