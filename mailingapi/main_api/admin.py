from django.contrib import admin
from .models import Message, Client, Delivery
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['send_date', 'sending_status', 'delivery', 'client']
    filter = ['send_date']



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['tel', 'code', 'tag', 'timezone']


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['date_of_creation', 'message', 'final_date', 'tag', 'code']
    filter = ['date_of_creation']