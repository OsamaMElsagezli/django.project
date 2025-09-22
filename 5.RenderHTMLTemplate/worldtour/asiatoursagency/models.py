from django.db import models

# Create your models here.
class Tour (models.Model):
    # We need origin country, destination, number of nights, and the price for that tour.
    origin_contry = models.CharField(max_length=64)
    destination_contry = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    # This is a string representaion of the Tours.

    def __str__(self):
        return (f"ID:{self.id}: From {self.origin_contry} To {self.destination_contry}, {self.number_of_nights} night cost $ {self.price}")


    