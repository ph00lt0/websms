from django.contrib import admin
from .models import TwilioConfig, PhoneOwnership

admin.site.register(TwilioConfig)
admin.site.register(PhoneOwnership)
