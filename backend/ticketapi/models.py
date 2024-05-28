from django.db import models
from api.models import User
from flightapi.models import Flight


# Create your models here.
class Ticket(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    flight= models.ForeignKey(Flight, on_delete=models.CASCADE)