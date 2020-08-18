from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('invitation/', views.InvitationView.as_view(), name='invitation'),
    path('', views.index, name='index'),
]
