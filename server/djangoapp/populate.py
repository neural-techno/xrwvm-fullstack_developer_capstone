from .models import CarMake, CarModel


def initiate():
    """
    Initializes the car makes and car models in the database.

    This function creates instances of car manufacturers (CarMake)
    and corresponding car models (CarModel) using pre-defined data.
    """

    car_make_data = [
        {
            "name": "NISSAN", 
            "description": "Great cars. Japanese technology", 
            "country_of_origin": "Japan",
            "established_date": "1933-12-26"
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology",
            "country_of_origin": "Germany",
            "established_date": "1926-06-28"
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology",
            "country_of_origin": "Germany",
            "established_date": "1909-07-16"
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology",
            "country_of_origin": "South Korea",
            "established_date": "1944-12-11"
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology",
            "country_of_origin": "Japan",
            "established_date": "1937-08-28"
        },
    ]

    # Create CarMake instances and store in a list
    car_make_instances = []
    for data in car_make_data:
        car_make_instance = CarMake.objects.create(
            name=data['name'],
            description=data['description'],
            country_of_origin=data['country_of_origin'],
            established_date=data['established_date']
        )
        car_make_instances.append(car_make_instance)

    # Create CarModel instances with corresponding CarMake instances
    car_model_data = [
    {
        "name": "Pathfinder",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[0],
        "engine_type": "V6",
        "fuel_type": "PETROL",
        "color": "Blue",
        "price": 35000.00,
        "mileage": 22.5,
        "horsepower": 300,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "Qashqai",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[0],
        "engine_type": "Electric",
        "fuel_type": "ELECTRIC",
        "color": "White",
        "price": 45000.00,
        "mileage": 30.0,
        "horsepower": 200,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "XTRAIL",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[0],
        "engine_type": "V8",
        "fuel_type": "PETROL",
        "color": "Red",
        "price": 42000.00,
        "mileage": 25.0,
        "horsepower": 350,
        "transmission": "MANUAL"
    },
    {
        "name": "A-Class",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[1],
        "engine_type": "Electric",
        "fuel_type": "ELECTRIC",
        "color": "Black",
        "price": 50000.00,
        "mileage": 28.0,
        "horsepower": 250,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "C-Class",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[1],
        "engine_type": "V6",
        "fuel_type": "DIESEL",
        "color": "Silver",
        "price": 55000.00,
        "mileage": 26.5,
        "horsepower": 400,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "E-Class",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[1],
        "engine_type": "V8",
        "fuel_type": "PETROL",
        "color": "Blue",
        "price": 60000.00,
        "mileage": 24.5,
        "horsepower": 500,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "A4",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[2],
        "engine_type": "V6",
        "fuel_type": "PETROL",
        "color": "White",
        "price": 42000.00,
        "mileage": 27.0,
        "horsepower": 350,
        "transmission": "MANUAL"
    },
    {
        "name": "A5",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[2],
        "engine_type": "V8",
        "fuel_type": "HYBRID",
        "color": "Red",
        "price": 46000.00,
        "mileage": 25.0,
        "horsepower": 400,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "A6",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[2],
        "engine_type": "Electric",
        "fuel_type": "ELECTRIC",
        "color": "Blue",
        "price": 50000.00,
        "mileage": 30.0,
        "horsepower": 350,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "Sorrento",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[3],
        "engine_type": "V6",
        "fuel_type": "PETROL",
        "color": "Black",
        "price": 38000.00,
        "mileage": 20.0,
        "horsepower": 300,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "Carnival",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[3],
        "engine_type": "V8",
        "fuel_type": "DIESEL",
        "color": "White",
        "price": 47000.00,
        "mileage": 22.0,
        "horsepower": 350,
        "transmission": "MANUAL"
    },
    {
        "name": "Cerato",
        "type": "Sedan",
        "year": 2023,
        "car_make": car_make_instances[3],
        "engine_type": "V6",
        "fuel_type": "PETROL",
        "color": "Green",
        "price": 23000.00,
        "mileage": 28.0,
        "horsepower": 250,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "Corolla",
        "type": "Sedan",
        "year": 2023,
        "car_make": car_make_instances[4],
        "engine_type": "Electric",
        "fuel_type": "ELECTRIC",
        "color": "Blue",
        "price": 35000.00,
        "mileage": 30.0,
        "horsepower": 300,
        "transmission": "AUTOMATIC"
    },
    {
        "name": "Camry",
        "type": "Sedan",
        "year": 2023,
        "car_make": car_make_instances[4],
        "engine_type": "V6",
        "fuel_type": "HYBRID",
        "color": "Yellow",
        "price": 40000.00,
        "mileage": 28.0,
        "horsepower": 350,
        "transmission": "MANUAL"
    },
    {
        "name": "Kluger",
        "type": "SUV",
        "year": 2023,
        "car_make": car_make_instances[4],
        "engine_type": "V8",
        "fuel_type": "DIESEL",
        "color": "Red",
        "price": 45000.00,
        "mileage": 24.0,
        "horsepower": 400,
        "transmission": "AUTOMATIC"
    }]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            engine_type=data['engine_type'],
            fuel_type=data['fuel_type'],
            color=data['color'],
            price=data['price'],
            mileage=data['mileage'],
            horsepower=data['horsepower'],
            transmission=data['transmission']
        )
