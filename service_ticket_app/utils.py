from upcoming.models import Post
from ticket.models import *
from django.contrib.auth.models import User

# Tickets

def ticket_count(request):
    """
    Returns the number of All Tickets related to the account of the logged in user
    """
    count = Ticket.objects.filter(account=request.user.accountuser.account).count()
    return count

def all_tickets(request):
    """
    Returns All Tickets related to the account of the logged in user
    """
    all_tickets = Ticket.objects.filter(account=request.user.accountuser.account)
    return all_tickets

def todays_tickets_count(request):
    """
    Returns the number of tickets scheduled for today related to the account of the logged in user
    """
    todays_tickets_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today()).count()
    return todays_tickets_count

def todays_tickets(request):
    """
    Returns tickets scheduled for today related to the account of the logged in user
    """
    todays_tickets = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today())
    return todays_tickets

def in_progress_count(request):
    """
    Returns the number of tickets scheduled for today that are currently in progress related to the account of the logged in user. start_time has been checked and end_time has not
    """
    in_progress_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today(),start_job=True,completed=False).count()
    return in_progress_count

def completed_today_tickets_count(request):
    """
    Returns the number of tickets scheduled for today that have been completed and related to the account of the logged in user
    """
    completed_today_tickets_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today(), start_job=True, completed=True).count()
    return completed_today_tickets_count

# Tech Tickets

def tech_ticket_count(request):
    """
    Returns the number of all tickets belonging to the logged in user
    """
    count = Ticket.objects.filter(account=request.user.accountuser.account, assigned=request.user.accountuser).count()
    return count

def tech_tickets(request):
    """
    Returns all tickets belonging to the logged in user
    """
    tech_tickets = Ticket.objects.filter(account=request.user.accountuser.account, assigned=request.user.accountuser)
    return tech_tickets


def tech_todays_tickets_count(request):
    """
    Returns the number of all tickets scheduled for today belonging to the logged in user
    """
    tech_todays_tickets_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today(), assigned=request.user.accountuser).count()
    return tech_todays_tickets_count


def tech_todays_tickets(request):
    """
    Returns all tickets scheduled for today belonging to the logged in user
    """
    tech_todays_tickets = Ticket.objects.filter(account=request.user.accountuser.account, assigned=request.user.accountuser, schedule=datetime.date.today())
    return tech_todays_tickets

def tech_completed_today_tickets_count(request):
    """
    Returns the number of all tickets scheduled for today and completed belonging to the logged in user
    """
    tech_completed_today_tickets_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today(), start_job=True, completed=True, assigned=request.user.accountuser).count()
    return tech_completed_today_tickets_count

# Other Models

def posts(request):
    """
    Returns all posts in upcoming related to the account of the logged in users account - admins only
    """
    posts = Post.objects.filter(account=request.user.accountuser.account)
    return posts

def ticket_type(request):
    """
    Returns type of tickets belonging to the account of the logged in user
    """
    tickettype = TicketType.objects.filter(account=request.user.accountuser.account)
    return tickettype

def company(request):
    """
    Returns all companies belonging to the account of the logged in user
    """
    company = Company.objects.filter(account=request.user.accountuser.account)
    return company

def company_count(request):
    """
    Returns the number of companies belonging to the account of the logged in user
    """
    company_count = Company.objects.filter(account=request.user.accountuser.account).count()
    return company_count

def customer(request):
    """
    Returns all customers belonging to the account of the logged in user
    """
    customer = Customer.objects.filter(account=request.user.accountuser.account)
    return customer

def customer_count(request):
    """
    Returns the number of customers belonging to the account of the logged in user
    """
    customer = Customer.objects.filter(account=request.user.accountuser.account).count()
    return customer

def jobsite(request):
    """
    Returns all jobsites belonging to the account of the logged in user
    """
    jobsite = Jobsite.objects.filter(account=request.user.accountuser.account)
    return jobsite

def jobsite_count(request):
    """
    Returns the number of jobsites belonging to the account of the logged in user
    """
    jobsite_count = Jobsite.objects.filter(account=request.user.accountuser.account).count()
    return jobsite_count

def service_provided(request):
    """
    Returns all the services the account provides belonging to the account of the logged in user
    """
    serviceprovided = ServiceProvided.objects.filter(account=request.user.accountuser.account)
    return serviceprovided

def ticket(request):
    """
    Returns all tickets belonging to the account of the logged in user
    """
    ticket = Ticket.objects.filter(account=request.user.accountuser.account)
    return ticket

def user_count(request):
    """
    Returns the amount of users in a company
    """
    user_count = AccountUser.objects.filter(account=request.user.accountuser.account).count()
    return user_count