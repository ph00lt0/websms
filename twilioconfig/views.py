from django.http import HttpResponse
from django.shortcuts import render, reverse
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
    config = TwilioConfig.objects.filter(user=request.user)[0]

    if request.method == "POST":
         sid = request.POST['sid']
         token = request.POST['token']

         configs = TwilioConfig.objects.filter(user=request.user)
         if configs: # if some items are found in the database
             configs.update(sid=sid, token=token)
             config = configs[0]
         else:
              config = TwilioConfig(sid=sid, token=token, user=request.user)
              config.save()


    context = {
        'config': config
    }

    return render(request, 'configure.html', context)

