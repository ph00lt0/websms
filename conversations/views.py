from django.shortcuts import render
from .models import Conversation, Message


# Create your views here.


def conversations(request):
    conversation_list = Conversation.objects.filter(user=request.user)
    if request.method == "POST":
        from_number = request.POST["from_number"]
        to_number = request.POST["to_number"]
        existing_conversations = Conversation.objects.filter(user=request.user, from_number=from_number,
                                                             to_number=to_number)
        if existing_conversations:
            context = {
                'error': 'already exist'
            }
        else:
            contact = Conversation(from_number=from_number, to_number=to_number, user=request.user)
            contact.save()
            conversation_list = Conversation.objects.filter(user=request.user)

            print(conversation_list)
    context = {
        'conversations': conversation_list
    }
    return render(request, 'conversations/conversations.html', context)


def conversation(request, uuid):
    message_list = Message.objects.filter(conversation_id=uuid, conversation__user=request.user)
    if request.method == "POST":
        message = request.POST['message']
        messages = Message(msg_content=message, conversation_id=uuid)
        messages.save()
        message_list = Message.objects.filter(conversation__user=request.user, conversation_id=uuid)

    context = {
        'messages': message_list
    }
    return render(request, 'conversations/conversation.html', context)
