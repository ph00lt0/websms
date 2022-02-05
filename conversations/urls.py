from django.urls import path
from . import views

app_name = 'conversations'

urlpatterns = [
    path('conversations/', views.conversations),

]
