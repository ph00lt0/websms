from django.db import models
from django.contrib.auth.models import User
import uuid
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Conversation(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    internal = PhoneNumberField(null=False, blank=False)
    external = PhoneNumberField(null=False, blank=False)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    msg_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    outward = models.BooleanField(default=True)
