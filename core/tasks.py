from celery import shared_task
from newsscraper.celery  import app as celery_app

# allows you to call this function asynchronously


@shared_task
def send_mass_emails(recipient):
    print("Doing it")


@celery_app.task
def send_scheduled_emails():
    # get all those email addresses
    pass
