from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
import os
from twilio.rest import Client
from conversations.models import Conversation, Message
from .models import TwilioConfig, PhoneOwnership

# @validate_twilio_request
@csrf_exempt
def receive(request):
    if request.method == "POST":
        from_number = request.POST['From'] #change to form
        to_number = request.POST['To']
        message = request.POST['Body']

        existing_conversations = Conversation.objects.filter(from_number=external, to_number=internal)
        if existing_conversations:
            conversation = existing_conversations[0]
        else:
            owners = PhoneOwnership.objects.filter(number=to_number)
            if owners:
              conversation = Conversation(from_number=external, to_number=internal, user=owners[0].user)
              conversation.save()
            else:
               return HttpResponse("Bad request: phone number not owned", status=400)

        # store message
        messages = Message(msg_content=message, outward=False, conversation=conversation)
        messages.save()

        return HttpResponse("Message received", status=200)
    else:
        return HttpResponse("Method not allowed", status=405)


def updateNumbers(request):
    config = TwilioConfig.objects.filter(user=request.user)[0]
    client = Client(config.sid, config.token)
    number_list = client.incoming_phone_numbers.list()

    PhoneOwnership.objects.filter(user=request.user).delete()
    for number in number_list:
          # Set the webhook for the phone number
         incoming_phone_number = client.incoming_phone_numbers(number.sid).update(sms_url='https://hackaway.software/twilio/receive')
         phone = PhoneOwnership(user=request.user, number=number.phone_number)
         phone.save()

    context = {
       'config': config
    }
    return render(request, 'configure.html', context)


def configure(request):
    config = None
    configs = TwilioConfig.objects.filter(user=request.user)
    if configs: # if some items are found in the database
        config = TwilioConfig.objects.filter(user=request.user)[0]


    if request.method == "POST":
         sid = request.POST['sid']
         token = request.POST['token']

#          incoming_phone_number = client.incoming_phone_numbers.create(
#             sms_url='https://hackaway.software/twilio/receive',
#             phone_number='+447700153842'
#          )

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

         return updateNumbers(request)

    context = {
        'config': config
    }

    return render(request, 'configure.html', context)

