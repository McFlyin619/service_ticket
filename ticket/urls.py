from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'ticket_app'
urlpatterns = [
    path('new-ticket/', views.TicketCreateView.as_view(), name='new_ticket'),
    path('tickets/', views.TicketListView.as_view(), name='all_tickets'),
    path('ticket/<pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('update/<pk>/', views.TicketUpdateView.as_view(), name='ticket_update'),
    path('update-<pk>/', views.TechTicketUpdateView.as_view(), name='tech_ticket_update'),
    path('delete/<pk>', views.TicketDeleteView.as_view(), name='ticket_delete')
]