from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts import views

urlpatterns = [
    path('', views.user_login ,name='login')
]