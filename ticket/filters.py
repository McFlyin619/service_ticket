from django_filters.filters import ModelMultipleChoiceFilter, QuerySetRequestMixin
from accounts.models import AccountUser, AccountCompany
import django_filters
from django_filters.widgets import RangeWidget
from django.contrib.auth.models import User

from .models import Ticket


class TicketFilter(django_filters.FilterSet):
    # date range choice to filter tickets
    Date = django_filters.DateFromToRangeFilter(field_name='end_time', widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Ticket
        fields ={
            'ticket_number':['contains'],\
            }

        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # change the widget choices after initialization
        self.form.fields['Date'].label = 'Date for report'
        

