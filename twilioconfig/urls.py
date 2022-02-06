from django.urls import path
from . import views

app_name = 'twilioconfig'

urlpatterns = [
    path('receive/', views.receive, name='receive'),
    path('config/', views.configure, name='configure'),
]
