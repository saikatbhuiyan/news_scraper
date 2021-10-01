from celery import shared_task
from newsscraper.celery  import app as celery_app
from .scrapers import scrape


URL = "https://dev.to/search?q=django"


@celery_app.task
def scrape_dev_to():
    scrape(URL)
    return


@shared_task  # allows us to call this function asynchronously
def scrape_async():
    scrape(URL)
    return

# allows us to call this function asynchronously


# @shared_task
# def send_mass_emails(recipient):
#     print("Doing it")


# @celery_app.task
# def send_scheduled_emails():
#     # get all those email addresses
#     pass
