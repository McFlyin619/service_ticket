from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('add-user/',views.add_user, name='add_user'),
    path('users/',views.UserListView.as_view(), name='users'),
    path('delete-user-<pk>/', views.UserDeleteView.as_view(), name='delete_user')
]