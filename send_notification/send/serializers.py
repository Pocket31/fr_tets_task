from rest_framework import serializers
from .models import Client, Sending, Message


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class SendingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sending
        fields = '__all__'


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
