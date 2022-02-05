from django.db import models
from django.contrib.auth.models import User
import uuid
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Conversations(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, related_name="Sender", on_delete=models.CASCADE)
    from_number = PhoneNumberField(null=False, blank=False)
    to_number = PhoneNumberField(null=False, blank=False)


class Message(models.Model):
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    msg_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
