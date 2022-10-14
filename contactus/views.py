from django.shortcuts import render
from django.http import HttpResponse
import datetime

from contactus.models import Contactus


def index(request):
    if request.method == 'POST':
        contactus = Contactus()

        fname = request.POST.get('fname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactus.fname = fname
        contactus.email = email
        contactus.subject = subject
        contactus.message = message
        contactus.msg_date = datetime.date.today()

        contactus.save()

        return HttpResponse('Submitted successfully')

    return render(request, 'aptech_consult/contactus.html')
