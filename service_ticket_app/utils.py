from upcoming.models import Post
from ticket.models import *

# Tickets

def ticket_count(request):
    count = Ticket.objects.filter(account=request.user.accountuser.account).count()
    return count

def all_tickets(request):
    all_tickets = Ticket.objects.filter(account=request.user.accountuser.account)
    return all_tickets

def todays_tickets_count(request):
    todays_tickets_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today()).count()
    return todays_tickets_count

def todays_tickets(request):
    todays_tickets = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today())
    return todays_tickets

def in_progress_count(request):
    in_progress_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today(),start_job=True,completed=False).count()
    return in_progress_count

def completed_today_tickets_count(request):
    completed_today_tickets_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today(), start_job=True, completed=True).count()
    return completed_today_tickets_count

# Tech Tickets

def tech_ticket_count(request):
    count = Ticket.objects.filter(account=request.user.accountuser.account, assigned=request.user.accountuser).count()
    return count

def tech_tickets(request):
    tech_tickets = Ticket.objects.filter(account=request.user.accountuser.account, assigned=request.user.accountuser)
    return tech_tickets


def tech_todays_tickets_count(request):
    tech_todays_tickets_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today(), assigned=request.user.accountuser).count()
    return tech_todays_tickets_count


def tech_todays_tickets(request):
    tech_todays_tickets = Ticket.objects.filter(account=request.user.accountuser.account, assigned=request.user.accountuser, schedule=datetime.date.today())
    return tech_todays_tickets

def tech_completed_today_tickets_count(request):
    tech_completed_today_tickets_count = Ticket.objects.filter(account=request.user.accountuser.account, schedule=datetime.date.today(), start_job=True, completed=True, assigned=request.user.accountuser).count()
    return tech_completed_today_tickets_count

# Other Models

def posts(request):
    posts = Post.objects.filter(account=request.user.accountuser.account)
    return posts

def ticket_type(request):
    tickettype = TicketType.objects.filter(account=request.user.accountuser.account)
    return tickettype

def company(request):
    company = Company.objects.filter(account=request.user.accountuser.account)
    return company

def customer(request):
    customer = Customer.objects.filter(account=request.user.accountuser.account)
    return customer

def jobsite(request):
    jobsite = Jobsite.objects.filter(account=request.user.accountuser.account)
    return jobsite

def service_provided(request):
    serviceprovided = ServiceProvided.objects.filter(account=request.user.accountuser.account)
    return serviceprovided