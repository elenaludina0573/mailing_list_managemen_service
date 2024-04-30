from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.triggers.interval import IntervalTrigger
from service.utils import mailings


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'default')

    scheduler.add_job(
        mailings,
        trigger=IntervalTrigger(minutes=1),
        id='send_messages',
        max_instances=1,
        replace_existing=True
    )

    scheduler.start()
