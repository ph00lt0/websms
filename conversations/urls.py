from django.urls import path
from . import views

app_name = 'conversations'

urlpatterns = [
    path('', views.conversations, name='conversations'),
    path('<uuid:uuid>/', views.conversation, name='conversation'),
]
