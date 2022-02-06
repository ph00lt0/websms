from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
import os
from twilio.rest import Client
from .models import TwilioConfig


# @validate_twilio_request
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
    config = None
    configs = TwilioConfig.objects.filter(user=request.user)
    if configs: # if some items are found in the database
        config = TwilioConfig.objects.filter(user=request.user)[0]


    if request.method == "POST":
         sid = request.POST['sid']
         token = request.POST['token']

         client = Client(sid, token)

#          incoming_phone_number = client.incoming_phone_numbers.create(
#             sms_url='https://hackaway.software/twilio/receive',
#             phone_number='+447700153842'
#          )

         number_list = client.incoming_phone_numbers.list()

         for number in number_list:
              # Set the webhook for the phone number
             incoming_phone_number = client.incoming_phone_numbers(number.sid).update(sms_url='https://hackaway.software/twilio/receive')

         # Obtain information
         # incoming_phone_number = client.incoming_phone_numbers.create(phone_number='+447700153842')
         # print(incoming_phone_number.sid)


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

