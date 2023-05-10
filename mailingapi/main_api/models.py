from django.db import models
import datetime
import pytz
import django.core.validators as val
from django.utils import timezone, dateformat

# Create your models here.


class Delivery(models.Model):

    date_of_creation = models.DateTimeField(null=False,
                                            default=timezone.now,
                                            verbose_name='creation time')
    message = models.TextField(null=False, default='', verbose_name='message')

    final_date = models.DateTimeField(null=True, blank=True, verbose_name='final time', default=None)

    code = models.CharField(max_length=3, verbose_name="code of client", blank=True, default='')

    tag = models.CharField(max_length=20, verbose_name="tag of client", blank=True, default='')

    def save(self, *args, **kwargs):
        if self.final_date is None:
            self.final_date = self.date_of_creation + timezone.timedelta(1)
        super(Delivery, self).save(*args, **kwargs)

    def __str__(self):
        return f'Delivery {self.pk}'

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'




class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    tel = models.CharField(max_length=11,
                           default=None,
                           validators=[val.RegexValidator(
                                            regex=r"^7\d{10}$",
                                            message="The client's phone number "
                                                    "in the format 7XXXXXXXXXX "
                                                    "(X - number from 0 to 9)")],
                           verbose_name='tel')

    code = models.CharField(max_length=3, default=None, verbose_name='code')

    tag = models.CharField(max_length=20, default=None, verbose_name='tag', null=True)

    timezone = models.CharField(
        verbose_name="Time zone", max_length=32, choices=TIMEZONES, default="UTC"
    )

    def __str__(self):
        return f'Client {self.pk}'

    class Meta:

        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

class Message(models.Model):

    STATUS = [
        ('sent', 'sent'),
        ('not sent', 'not sent')
    ]

    send_date = models.DateTimeField(default=timezone.now)
    sending_status = models.CharField(
        verbose_name="Sending status", max_length=15, choices=STATUS, default='not sent'
    )
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name="delivery")

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client")

    def __str__(self):
        return f'Message {self.pk}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'