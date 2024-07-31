from django.db import models

# Create your models here.
class Flight(models.Model):
    fightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimateTimeOfDeparture = models.TimeField()

    def __str__(self):
        return self.fightNumber

class Passanger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.firstName+self.lastName

class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passanger = models.OneToOneField(Passanger,on_delete=models.CASCADE)