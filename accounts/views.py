
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from service_ticket_app import utils
from service_ticket_app.utils import *

from accounts.models import *

from . import forms

# Create your views here.


@login_required
def add_user(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserCreateForm(data=request.POST)
        account_user_form = forms.AccountUserForm(data=request.POST)

        if user_form.is_valid() and account_user_form.is_valid():

            new_user = user_form.save()
            new_user.set_password(new_user.password)
            new_user.save()
            # adds logged in users account to newly created users account
            user_account = account_user_form.save(commit=False)
            user_account.user = new_user
            user_account.account = request.user.accountuser.account

            user_account.save()
            registered = True
        
        else:
            print(user_form.errors,account_user_form.errors)

    else:
        user_form = forms.UserCreateForm()
        account_user_form = forms.AccountUserForm()   
    
    ticket_count = utils.ticket_count(request)
    tech_ticket_count = utils.tech_ticket_count(request)
    
    context = {
        'registered':registered,
        'user_form':user_form,
        'account_user_form':account_user_form,
        'ticket_count':ticket_count,
        'tech_ticket_count':tech_ticket_count,
    }

    return render(request,'accounts/add_user.html',context=context) 

class UserListView(ListView,LoginRequiredMixin):
    model = AccountUser
    context_object_name = 'accountuser'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_count'] = ticket_count(self.request)
        context['tech_ticket'] = tech_tickets(self.request)
        context['tech_ticket_count'] = tech_ticket_count(self.request)
        context['accountuser'] = AccountUser.objects.filter(account=self.request.user.accountuser.account)
        context['todays_tickets'] = todays_tickets(self.request)
        context['tech_todays_tickets'] = tech_todays_tickets(self.request)
        context['todays_tickets_count'] = todays_tickets_count(self.request)
        context['in_progress_count'] = in_progress_count(self.request)
        context['completed_today_tickets_count'] = completed_today_tickets_count(self.request)
        context['tech_todays_tickets_count'] = tech_todays_tickets_count(self.request)
        context['tech_completed_today_tickets_count'] = tech_completed_today_tickets_count(self.request)
        return context 

class UserDeleteView(DeleteView,LoginRequiredMixin):
    model = AccountUser
    success_url = reverse_lazy('accounts:users')
