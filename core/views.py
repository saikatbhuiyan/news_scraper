from django.shortcuts import render
from core.tasks import send_mass_emails

# Create your views here.


def mass_email_view(request):
    recipient = 'fuewhfuew@fewfe.com'
    send_mass_emails.delay(recipient)
