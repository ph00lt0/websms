import os
from twilio.rest import Client


def sent(request):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = request['message']
    to = request['to']

    message = client.messages.create(
        body=message,
        from_='+447700153842',  # should change to choice later
        # media_url=['https://demo.twilio.com/owl.png'], could be added later for MMS
        to=to
    )

    return message.sid

