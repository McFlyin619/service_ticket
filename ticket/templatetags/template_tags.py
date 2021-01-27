import datetime
from django import template

register = template.Library()

@register.filter()
def addDays(days):
   newDate = datetime.date.today() + datetime.timedelta(days=days)
   return newDate

@register.filter()
def percentage(part, whole):
   if whole == 0:
      return 0
   return 100 * float(part)/float(whole)

def reg():
       pass
