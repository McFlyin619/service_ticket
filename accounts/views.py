from django.shortcuts import render
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy, reverse
from django.http import request, HttpResponse, HttpResponseRedirect
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
            return HttpResponse('Username or Password does not match our records. Please try again.')

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

    return render(request,'',{ 
    'registered':registered}) 