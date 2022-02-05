from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class User:
    username = models.CharField(50)

class PhoneContacts(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be less than 15 characters!")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # vali



class Message(models.Model):
    from_number = models.ForeignKey(User, related_name="Sender")
    to_number = models.ForeignKey(User, related_name="Receiver")
    msg_content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


