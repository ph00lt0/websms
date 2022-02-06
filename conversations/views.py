from django.shortcuts import render, reverse
from .models import Conversation, Message
from twilioconfig.models import TwilioConfig
from twilio.rest import Client
from django.http import HttpResponseRedirect


def conversations(request):
    conversation_list = Conversation.objects.filter(user=request.user)
    if request.method == "POST":
        from_number = request.POST["from_number"]
        to_number = request.POST["to_number"]
        existing_conversations = Conversation.objects.filter(user=request.user, internal=from_number,
                                                             external=to_number)
        if existing_conversations:
            context = {
                'error': 'already exist'
            }
        else:
            contact = Conversation(internal=from_number, external=to_number, user=request.user)
            contact.save()
            conversation_list = Conversation.objects.filter(user=request.user)

            print(conversation_list)
    context = {
        'conversations': conversation_list
    }
    return render(request, 'conversations/conversations.html', context)


def conversation(request, uuid):
    message_list = Message.objects.filter(conversation_id=uuid, conversation__user=request.user)
    config = None
    configs = TwilioConfig.objects.filter(user=request.user)
    if configs: # if some items are found in the database
        if request.method == "POST":
            message = request.POST['message']
            config = TwilioConfig.objects.filter(user=request.user)[0]

            client = Client(config.sid, config.token)
            conversation = Conversation.objects.get(uuid=uuid)

            twilio_message = client.messages.create(
                body=message,
                from_=str(conversation.internal),  # should change to choice later
                # media_url=['https://demo.twilio.com/owl.png'], could be added later for MMS
                to=str(conversation.external)
            )

            messages = Message(msg_content=message, conversation_id=uuid)
            messages.save()
            message_list = Message.objects.filter(conversation__user=request.user, conversation_id=uuid)

        context = {
            'messages': message_list
        }
        return render(request, 'conversations/conversation.html', context)
    else:
        return HttpResponseRedirect(reverse('twilioconfig:configure'))

