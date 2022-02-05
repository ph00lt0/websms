from django.urls import path
from . import views

app_name = 'twilio'

urlpatterns = [
    path('receive/', views.receive, name='receive'),
    path('config/', views.config, name='config'),
]
