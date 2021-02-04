from django.shortcuts import render
from django.http import request
from .forms import CompanyCreateForm, CustomerCreateForm, JobsiteCreateForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Customer,Company,Jobsite
from customer.forms import CustomerCreateForm
from service_ticket_app.utils import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CompanyCreateView(LoginRequiredMixin,CreateView):
    model = Company
    form_class = CompanyCreateForm

    def form_valid(self, form):
        form.instance.account = self.request.user.accountuser.account
        return super(CompanyCreateView, self).form_valid(form)
    
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

class CompanyListView(LoginRequiredMixin,ListView):
    model = Company
    context_object_name = 'company'

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
        context['company'] = company(self.request)
        return context

class CompanyUpdateView(LoginRequiredMixin,UpdateView):
    model = Company
    form_class = CompanyCreateForm

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

class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('customer:companies') 

class CustomerCreateView(LoginRequiredMixin,CreateView):
    model = Customer
    form_class = CustomerCreateForm

    def get_form(self, form_class=None):
        form = super(CustomerCreateView, self).get_form(form_class)
        form.fields['company'].queryset = Company.objects.filter(account=self.request.user.accountuser.account)
        return form

    def form_valid(self, form):
        form.instance.account = self.request.user.accountuser.account
        return super(CustomerCreateView, self).form_valid(form)
    
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

class CustomerListView(LoginRequiredMixin,ListView):
    model = Customer
    context_object_name = 'customer'

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
        context['customer'] = customer(self.request)
        return context

class CustomerUpdateView(LoginRequiredMixin,UpdateView):
    model = Customer
    form_class = CustomerCreateForm
    
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

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:customers') 
    
class JobsiteCreateView(LoginRequiredMixin,CreateView):
    model = Jobsite
    form_class = JobsiteCreateForm

    def form_valid(self, form):
        form.instance.account = self.request.user.accountuser.account
        return super(JobsiteCreateView, self).form_valid(form)
    
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

class JobsiteListView(LoginRequiredMixin,ListView):
    model = Jobsite
    context_object_name = 'jobsite'

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
        context['jobsite'] = jobsite(self.request)
        return context

class JobsiteUpdateView(LoginRequiredMixin,UpdateView):
    model = Jobsite
    form_class = JobsiteCreateForm

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

class JobsiteDeleteView(LoginRequiredMixin, DeleteView):
    model = Jobsite
    success_url = reverse_lazy('customer:jobsites')