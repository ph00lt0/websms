from django.db import models
from django.contrib.auth.models import User
import uuid
from phonenumber_field.modelfields import PhoneNumberField


class TwilioConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sid = models.CharField(max_length=40)
    token = models.CharField(max_length=40)
