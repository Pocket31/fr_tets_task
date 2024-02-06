from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, Sending, Message
from .serializers import ClientSerializers, SendingSerializers, MessageSerializers


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializers
    queryset = Client.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializers
    queryset = Message.objects.all()


class SendingViewSet(viewsets.ModelViewSet):
    serializer_class = SendingSerializers
    queryset = Sending.objects.all()

    @action(methods=['get'], detail=False)
    def statistics(self, request):
        total_quantity = Sending.objects.count()
        sendings = Sending.objects.values('pk')
        statistic = {}

        for sending in sendings:
            quantity_delivered_message = Message.objects.filter(
                sending_id=sending['pk']).all().filter(status=1).count()
            quantity_not_delivered = Message.objects.filter(
                sending_id=sending['pk']).all().filter(status=0).count()
            statistic['Доставлено сообщений'] = quantity_delivered_message
            statistic['Не доставлено сообщений'] = quantity_not_delivered

        total_result = {'Всего рассылок': total_quantity,
                        'Результат': statistic}
        return Response(total_result)

    @action(methods=['get'], detail=True)
    def detail_statistics(self, request, pk):
        try:
            sendings = Sending.objects.get(pk=pk)
        except Sending.DoesNotExist:
            raise Http404
        detail_result = Message.objects.filter(sending=pk).all()
        return Response(MessageSerializers(detail_result, many=True).data)
