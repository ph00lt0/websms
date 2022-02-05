from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('receive/', views.login, name='receive'),
]
