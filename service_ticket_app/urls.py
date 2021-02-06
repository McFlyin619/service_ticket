"""service_ticket_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('customer.urls')),
    path('', include('ticket.urls')),
    path('',include('upcoming.urls')),
    path('',include('part.urls')),
    path('', views.TodayView.as_view(), name='today'),
    path('accounts/login/', views.user_login, name='login'),
    path('schedule/',views.CalendarView.as_view(), name='schedule'),
    path('logged_out/',views.user_logout, name='user_logout'),
]
