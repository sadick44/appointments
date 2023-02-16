from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    appointement_date = models.DateTimeField()
