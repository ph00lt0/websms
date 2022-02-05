from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from twilio.rest import Client


@csrf_exempt
def receive(request):
    if request.method == "POST":

        from_ = request.form['From']
        to = request.form['To']
        message = request.form['Body']

        return HttpResponse("Message received", status=200)
    else:
        return HttpResponse("Method not allowed", status=405)
