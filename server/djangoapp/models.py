# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    """
    Represents a car make (e.g., Toyota, Ford, etc.).

    The CarMake model stores information about the car manufacturer,
    including the name, description, country of origin, and the date
    the brand was established.

    Attributes:
        name (str): The name of the car manufacturer.
        description (str): A description of the car manufacturer.
        country_of_origin (str, optional):
        established_date (date, optional):
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    """
    Represents a car model with a specific car make

    The CarModel model stores details about a specific model of a car,
    including its make, type, year, engine type, fuel type, color, price,
    mileage, horsepower, and transmission.

    Attributes:
        car_make (ForeignKey): 
        name (str): The name of the car model (e.g., Camry, A-Class).
        type (str): The type of the car (e.g., Sedan, SUV, Wagon).
        year (int): The year the car model was manufactured.
        engine_type (str, optional): The type of engine in the car.
        fuel_type (str): 
        color (str, optional): The color of the car.
        price (decimal, optional): The price of the car.
        mileage (float, optional): The mileage of the car.
        horsepower (int, optional): The horsepower of the car's engine.
        transmission (str): 
    """
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
    validators = [
        MaxValueValidator(2023),
        MinValueValidator(2015)
    ])
    engine_type = models.CharField(max_length=50, blank=True, null=True)
    fuel_type = models.CharField(
        max_length=20,
        choices=[
            ('PETROL', 'Petrol'),
            ('DIESEL', 'Diesel'),
            ('ELECTRIC', 'Electric'),
            ('HYBRID', 'Hybrid')
        ],
        default='PETROL'
    )
    color = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        blank=True, null=True
    )
    mileage = models.FloatField(blank=True, null=True)
    horsepower = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(
        max_length=20,
        choices=[('AUTOMATIC', 'Automatic'), ('MANUAL', 'Manual')],
        default='AUTOMATIC'
    )
    def __str__(self):
        return self.name
