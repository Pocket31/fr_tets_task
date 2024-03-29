from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Sending
from .task import sending_message


@receiver(signal=post_save, sender=Sending)
def sending_request(sender, instance=None, created=False, **kwargs):
    if created:
        scheduler = BackgroundScheduler()
        scheduler.start()
        if instance.to_send:
            scheduler.add_job(
                sending_message,
                trigger=CronTrigger(start_date=timezone.now()),
                args=[instance.id],
                id=f"_job",
                max_instances=1,
                replace_existing=True,
            )
        else:
            scheduler.add_job(
                sending_message,
                trigger=CronTrigger(start_date=instance.beginning),
                args=[instance.id],
                id=f"__job",
                max_instances=1,
                replace_existing=True,
            )
