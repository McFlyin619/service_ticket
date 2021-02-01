from django.http import request
from ticket.forms import TechTicketUpdateForm, TicketForm, TicketUpdateForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Ticket
from customer.forms import CustomerCreateForm
from service_ticket_app.utils import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TicketCreateView(LoginRequiredMixin,CreateView):
    model = Ticket
    form_class = TicketForm
    
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

def customer_popup(request):
    form = CustomerCreateForm(request.POST or None)
    if form.is_valid:
        instance = form.save()

        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_customer");</script>' % (instance.pk, instance))
    return render(request, 'customer/customer_form.html',{'form':form})

# @csrf_exempt
# def get_customer_id(request):
# 	if request.is_ajax():
# 		fname = request.GET['fname']
# 		customer_id = Customer.objects.get(fname=fname).id
# 		data = {'author_id':author_id,}
# 		return HttpResponse(json.dumps(data), content_type='application/json')
# 	return HttpResponse("/")

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
        return context 

class TicketTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TicketType
    success_url = reverse_lazy('ticket_app:ticket_type_list') 