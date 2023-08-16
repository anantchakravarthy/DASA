from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import date
from accounts.models import User

reason = (
    ('root_canal_treatment', "Root Canal Treatment"),
    ('impaction', "Impaction"),
    ('tooth_pain', "Tooth Pain"),
    ('cavity', "Cavity"),
    ('filling', "Filling"),
    ('crown_placement', "Crown Placement")
)
start_time = (
    ('9:00 AM', "9:00 AM"),
    ('10:00 AM', "10:00 AM"),
    ('11:00 AM', "11:00 AM"),
    ('12:00 PM', "12:00 PM"),
    ('1:00 PM', "1:00 PM"),
    ('2:00 PM', "2:00 PM"),
    ('3:00 PM', "3:00 PM"),
    ('4:00 PM', "4:00 PM"),
)
end_time = (
    ('10:00 AM', "10:00 AM"),
    ('11:00 AM', "11:00 AM"),
    ('12:00 PM', "12:00 PM"),
    ('1:00 PM', "1:00 PM"),
    ('2:00 PM', "2:00 PM"),
    ('3:00 PM', "3:00 PM"),
    ('4:00 PM', "4:00 PM"),
    ('5:00 PM', "5:00 PM"),
)



class Appointment(models.Model):
    user = models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    dentist = models.ForeignKey(User, related_name='dentist', on_delete=models.CASCADE, null=True)
    reason = models.CharField(choices=reason, max_length=100)
    message = models.TextField()
    date = models.DateField(default=date.today)
    start_time = models.CharField(choices=start_time, max_length=10)
    end_time = models.CharField(choices=end_time, max_length=10)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.first_name


class DentistLog(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    consultation_date = models.DateField(default=date.today)
    consultation_duration = models.CharField(max_length=15, null=True)
    consultation_details = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.appointment.user.first_name
