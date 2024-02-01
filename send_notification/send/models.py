from django.core.validators import RegexValidator
from django.db import models


class Sending(models.Model):
    date_time_start = models.DateTimeField(verbose_name="Начало рассылки")
    text_message = models.TextField(verbose_name="Текст сообщения")
    date_time_end = models.DateTimeField(verbose_name="Конец рассылки")
    phone_code = models.CharField(verbose_name="Код телефона")
    tag = models.CharField(verbose_name="Тег", blank=True)


class Client(models.Model):
    phone_validator = RegexValidator(
        regex=r'^7\w{10}$', message="Номер телефона в формате 7XXXXXXXXXX (X - цифра от 0 до 9)")
    number_phone = models.PositiveIntegerField(
        verbose_name="Номер телефона", validators=phone_validator)
    operator_code = models.CharField(verbose_name="Код мобильного оператора")
    tag = models.CharField(verbose_name="Тег", blank=True)
    time_zone = models.CharField(verbose_name='Часовой пояс', max_length=10)


class Message(models.Model):

    STATUS = [
        (1, "Доставлено"),
        (2, "Не доставлено"),
    ]

    date_time_send = models.DateTimeField(
        verbose_name="Дата и время отправки сообщения", auto_now_add=True)
    status = models.CharField(
        verbose_name='Статус отправки сообщения', max_length=10, choices=STATUS)
    sending = models.ForeignKey(
        Sending, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='messages')
