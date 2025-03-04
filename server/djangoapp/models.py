# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)  # Optional: field for the country of origin
    established_date = models.DateField(blank=True, null=True)  # Optional: field for the year when the brand was established

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    engine_type = models.CharField(max_length=50, blank=True, null=True)  # Engine type (e.g., V6, V8, Electric)
    fuel_type = models.CharField(max_length=20, choices=[('PETROL', 'Petrol'), ('DIESEL', 'Diesel'), ('ELECTRIC', 'Electric'), ('HYBRID', 'Hybrid')], default='PETROL')  # Fuel type
    color = models.CharField(max_length=30, blank=True, null=True)  # Car color
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Price of the car model
    mileage = models.FloatField(blank=True, null=True)  # Mileage (miles per gallon or km per liter)
    horsepower = models.IntegerField(blank=True, null=True)  # Engine horsepower
    transmission = models.CharField(max_length=20, choices=[('AUTOMATIC', 'Automatic'), ('MANUAL', 'Manual')], default='AUTOMATIC')  # Transmission type
    def __str__(self):
        return self.name  # Return the name as the string representation
