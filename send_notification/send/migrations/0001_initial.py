# Generated by Django 5.0.1 on 2024-02-05 18:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_phone', models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(message='Номер телефона в формате 7XXXXXXXXXX (X - цифра от 0 до 9)', regex='^7\\w{10}$')], verbose_name='Номер телефона')),
                ('operator_code', models.CharField(max_length=5, verbose_name='Код мобильного оператора')),
                ('tag', models.CharField(blank=True, max_length=15, verbose_name='Тег')),
                ('time_zone', models.CharField(max_length=10, verbose_name='Часовой пояс')),
            ],
        ),
        migrations.CreateModel(
            name='Sending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_start', models.DateTimeField(verbose_name='Начало рассылки')),
                ('text_message', models.TextField(verbose_name='Текст сообщения')),
                ('date_time_end', models.DateTimeField(verbose_name='Конец рассылки')),
                ('phone_code', models.CharField(max_length=5, verbose_name='Код телефона')),
                ('tag', models.CharField(blank=True, max_length=5, verbose_name='Тег')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_send', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки сообщения')),
                ('status', models.CharField(choices=[(1, 'Доставлено'), (2, 'Не доставлено')], max_length=10, verbose_name='Статус отправки сообщения')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='send.client')),
                ('sending', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='send.sending')),
            ],
        ),
    ]
