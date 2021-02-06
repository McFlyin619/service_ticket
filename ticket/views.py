from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from service_ticket_app.utils import *

from ticket.forms import TechTicketUpdateForm, TicketForm, TicketUpdateForm

from .models import Ticket

# Create your views here.

class TicketCreateView(LoginRequiredMixin,CreateView):
    model = Ticket
    form_class = TicketForm
    
    def get_form(self, form_class=None):
        form = super(TicketCreateView, self).get_form(form_class)
        form.fields['assigned'].queryset = AccountUser.objects.filter(account=self.request.user.accountuser.account)
        form.fields['t_customer'].queryset = Customer.objects.filter(account=self.request.user.accountuser.account)
        form.fields['t_jobsite'].queryset = Jobsite.objects.filter(account=self.request.user.accountuser.account)
        form.fields['department'].queryset = ServiceProvided.objects.filter(account=self.request.user.accountuser.account)
        form.fields['t_type'].queryset = TicketType.objects.filter(account=self.request.user.accountuser.account)
        return form

    def form_valid(self, form):
        form.instance.account = self.request.user.accountuser.account
        return super(TicketCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        context['company_count'] = company_count(self.request)
        context['customer_count'] = customer_count(self.request)
        context['jobsite_count'] = jobsite_count(self.request)
        return context

class TicketListView(LoginRequiredMixin,ListView):
    model = Ticket
    context_object_name = 'ticket'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_ticket'] = tech_tickets(self.request)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        context['ticket'] = ticket(self.request)
        return context 
    
class TicketDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'ticket'
    model = Ticket
    template_name = 'ticket/ticket_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        context['history'] = Ticket.objects.filter(t_jobsite=self.get_object().t_jobsite, account=self.request.user.accountuser.account, completed=True).order_by('end_time')
        return context  

class TicketUpdateView(LoginRequiredMixin,UpdateView):
    model = Ticket
    form_class = TicketUpdateForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        return context 

class TechTicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = TechTicketUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        return context

class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticket_app:all_tickets') 

class TicketTypeCreateView(LoginRequiredMixin, CreateView):
    model = TicketType
    fields = ('name',)

    def form_valid(self, form):
        form.instance.account = self.request.user.accountuser.account
        return super(TicketTypeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_ticket'] = tech_tickets(self.request)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        return context 

class TicketTypeListView(LoginRequiredMixin, ListView):
    model = TicketType
    context_object_name = 'tickettype'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_ticket'] = tech_tickets(self.request)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        context['tickettype'] = ticket_type(self.request)
        return context 

class TicketTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TicketType
    success_url = reverse_lazy('ticket_app:ticket_type_list') 

class ServiceProvidedCreateView(LoginRequiredMixin, CreateView):
    model = ServiceProvided
    fields = ('name',)

    def form_valid(self, form):
        form.instance.account = self.request.user.accountuser.account
        return super(ServiceProvidedCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_ticket'] = tech_tickets(self.request)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        return context 

class ServiceProvidedListView(LoginRequiredMixin, ListView):
    model = ServiceProvided
    context_object_name = 'serviceprovided'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_ticket'] = tech_tickets(self.request)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        context['serviceprovided'] = service_provided(self.request)
        return context 

class ServiceProvidedDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceProvided
    success_url = reverse_lazy('ticket_app:serviceprovided_list') 
