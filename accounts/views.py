from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy, reverse
from django.http import request, HttpResponse, HttpResponseRedirect
from service_ticket_app import utils
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.


def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('today'))

            else: 
                return HttpResponse('Account is not active!')
        
        else:
            print('someone tried to login unsuccessfully!')
            return HttpResponse('<h1 class="text-center">Username or Password does not match our records. Please try again.</h1>')

    else:
        return render(request, 'accounts/login.html')

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
    model = models.AccountUser
    context_object_name = 'accountuser'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_count'] = utils.ticket_count(self.request)
        context['tech_ticket'] = utils.tech_tickets(self.request)
        context['tech_ticket_count'] = utils.tech_ticket_count(self.request)
        context['accountuser'] = models.AccountUser.objects.filter(account=self.request.user.accountuser.account)
        return context 

class UserDeleteView(DeleteView,LoginRequiredMixin):
    model = models.AccountUser
    success_url = reverse_lazy('accounts:users')