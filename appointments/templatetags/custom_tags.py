from django import template
import datetime
from appointments.models import Appointment


register = template.Library()

@register.filter(name='is_time_available')
def is_time_available(day, time):
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    time = datetime.time(hour=int(hour), minute=int(minute))
    return Appointment.is_time_available(time, day)

@register.filter(name='appointment_booked_at_time')
def appointment_booked_at_time(day, time):
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    time = datetime.time(hour=int(hour), minute=int(minute))
    return Appointment.appointment_booked_at_time(time, day)

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 