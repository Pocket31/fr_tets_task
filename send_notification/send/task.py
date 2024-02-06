import os
import pytz
import datetime
import requests
from dotenv import load_dotenv
from models import Client, Message, Sending

load_dotenv()
URL = os.getenv('URL')
TOKEN = os.getenv('TOKEN')


def sending_message(self, data, client_id, sending_id, url=URL, token=TOKEN):
    header = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    sending = Sending.objects.filter(id=sending_id)
    client = Client.objects.filter(id=client_id)
    timezone = pytz.timezone(client.time_zone)
    now = datetime.datetime(timezone)

    if sending.date_time_start <= now.time() <= sending.date_time_end:
        try:
            requests.post(url=url + str(data['id']), headers=header, json=data)
        except requests.exceptions.RequestException as exc:
            raise self.retry(exc=exc)
        else:
            Message.objects.filter(id=data['id']).update(status=1)
    else:
        time = 24 - (int(now.time().strftime('%H:%M:%S')
                     [:2]) - int(sending.date_time_start.strftime('%H:%M:%S')[:2]))
        return self.retry(countdown=60 * 60 * time)
