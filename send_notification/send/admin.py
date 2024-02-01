from django.contrib import admin

# Register your models here.
from .models import Sending, Client, Message


admin.site.register(Sending)
admin.site.register(Client)
admin.site.register(Message)
