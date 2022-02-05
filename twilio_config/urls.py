from django.urls import path
from . import views

app_name = 'twilio_config'

urlpatterns = [
    path('receive/', views.receive, name='receive'),
    path('config/', views.configure, name='config'),
]
