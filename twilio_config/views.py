from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from twilio.rest import Client
from .models import TwilioConfig


@csrf_exempt
def receive(request):
    if request.method == "POST":

        from_ = request.form['From']
        to = request.form['To']
        message = request.form['Body']

        return HttpResponse("Message received", status=200)
    else:
        return HttpResponse("Method not allowed", status=405)


def configure(request):
    config = TwilioConfig.objects.filter(user=request.user)

    if request.method == "POST":
         sid = request.POST['sid']
         token = request.POST['token']

         config = TwilioConfig.objects.filter(user=request.user)
         if config: # if some items are found in the database
             config.update(sid, token)
         else:
              config = TwilioConfig.objects.create(sid, token, user=request.user)


    context = {
        'config': config
    }

    return render(request, 'twilio_config/configure', context)
