from ticket.models import ServiceProvided, Ticket, TicketType
from django.contrib import admin

# Register your models here.
admin.site.register(Ticket)
admin.site.register(TicketType)
admin.site.register(ServiceProvided)