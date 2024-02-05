from django.core.validators import RegexValidator
from django.db import models
# from django.utils import timezone


class Sending(models.Model):
    date_time_start = models.DateTimeField(verbose_name="Начало рассылки")
    text_message = models.TextField(verbose_name="Текст сообщения")
    date_time_end = models.DateTimeField(verbose_name="Конец рассылки")
    phone_code = models.CharField(verbose_name="Код телефона", max_length=5)
    tag = models.CharField(verbose_name="Тег", blank=True, max_length=15)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self) -> str:
        return f'Рассылка {self.id}'


class Client(models.Model):
    phone_validator = RegexValidator(
        regex=r'^7\w{10}$', message="Номер телефона в формате 7XXXXXXXXXX (X - цифра от 0 до 9)")
    number_phone = models.PositiveIntegerField(
        verbose_name="Номер телефона", validators=[phone_validator])
    operator_code = models.CharField(
        verbose_name="Код мобильного оператора", max_length=5)
    tag = models.CharField(verbose_name="Тег", blank=True, max_length=15)
    time_zone = models.CharField(verbose_name='Часовой пояс', max_length=10)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self) -> str:
        return f'Клиент с номером {self.number_phone}'


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
        Sending, on_delete=models.CASCADE, related_name='messages', verbose_name='Рассылка')
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='messages', verbose_name='Клиент')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self) -> str:
        return f'Сообщение: {self.sending} для клиента {self.client}'
