from django.urls import path
from . import views

app_name = 'twilioconfig'

urlpatterns = [
    path('receive/', views.receive, name='receive'),
    path('config/', views.configure, name='configure'),
    path('update/', views.updateNumbers, name='update_numbers'),
    path('obtain/', views.obtain_number, name='obtain_number'),
]
