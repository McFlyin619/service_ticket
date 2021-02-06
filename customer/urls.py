
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from customer import views

app_name = 'customer_app'

urlpatterns = [
    
    # Customers
    path('customers/', views.CustomerListView.as_view(),name='customers'),
    path('add-customer/',views.CustomerCreateView.as_view(), name="add_customer"),
    path('delete-customer-<pk>/',views.CustomerDeleteView.as_view(), name='delete_customer'),
    path('edit-<pk>/', views.CustomerUpdateView.as_view(), name='edit_customer'),
    # Companies
    path('companies/', views.CompanyListView.as_view(),name='companies'),
    path('add-company/',views.CompanyCreateView.as_view(), name="add_company"),
    path('delete-company-<pk>/',views.CompanyDeleteView.as_view(), name='delete_company'),
    path('company-edit-<pk>/', views.CompanyUpdateView.as_view(), name='edit_company'),
    # Jobsites
    path('jobsites/', views.JobsiteListView.as_view(),name='jobsites'),
    path('add-jobsite/',views.JobsiteCreateView.as_view(), name="add_jobsite"),
    path('delete-jobsite-<pk>/',views.JobsiteDeleteView.as_view(), name='delete_jobsite'),
    path('jobsite-edit-<pk>/', views.JobsiteUpdateView.as_view(), name='edit_jobsite'),
]
