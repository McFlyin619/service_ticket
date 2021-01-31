from django.shortcuts import render
from service_ticket_app.utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.
class UpcomingView(LoginRequiredMixin, TemplateView):
    template_name = 'upcoming.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['tickets'] = all_tickets(self.request)
        context['tech_tickets_calendar'] = tech_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        return context