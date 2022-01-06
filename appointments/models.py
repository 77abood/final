from django.contrib.auth.models import User
from django.db import models

# Create your models here.

WEEK_DAYS = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (7, 'Sunday'),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    time =  models.TimeField(auto_now=False, auto_now_add=False)
    day = models.IntegerField(choices=WEEK_DAYS, null=True, default=None)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    vaccinated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vaccinated_appointments", null=True, default=None)
    vaccinated_date = models.DateTimeField(auto_now_add=False, null=True, default=None)

    @staticmethod
    def get_appoinments_except_day(day):
        appointments = Appointment.objects.filter(status = False).exclude(day = day)
        return appointments

    @staticmethod
    def is_time_available(time, day):
        for appointment in Appointment.objects.filter(status = False, day = day):
            if appointment.time == time:
                return False
        return True

    @staticmethod
    def appointment_booked_at_time(time, day):
        for appointment in Appointment.objects.filter(status = False, day = day):
            if appointment.time == time:
                return appointment
        return False