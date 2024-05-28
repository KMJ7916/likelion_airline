from django.db import models

# Create your models here.



class Flight(models.Model):
    # 출발 정보
    departure = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    departure_airport_code = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()

    # 도착 정보
    destination = models.CharField(max_length=100)
    destination_airport = models.CharField(max_length=100)
    destination_airport_code = models.CharField(max_length=100)
    destination_date = models.DateField()
    destination_time = models.TimeField()

    # 기타 정보
    duration = models.FloatField()
    airline = models.CharField(max_length=100)
    flight_class = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.airline} flight from {self.departure_airport_code} to {self.destination_airport_code} on {self.departure_date}"
