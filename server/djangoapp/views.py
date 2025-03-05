import json
import logging
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel
from .restapis import get_request, analyze_review_sentiments, post_review
from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create a `login_request` view to handle sign-in request
@csrf_exempt
def login_user(request):
    """Logs in the user if valid credentials are provided."""
    try:
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"userName": username, "status": "Authenticated"})

        return JsonResponse({"userName": username, "status": "Invalid credentials"})

    except json.JSONDecodeError:
        logger.exception("JSON decode error")
        return JsonResponse({"error": "Invalid JSON data"})
    except Exception as e:
        logger.exception("An error occurred while logging in")
        return JsonResponse({"error": str(e)})

# Create a `logout_request` view to handle sign-out request
def logout_user(request):
    """Logs out the user."""
    logout(request)
    return JsonResponse({"userName": ""})

# Create a `registration` view to handle sign-up request
@csrf_exempt
def registration(request):
    """Registers a new user if the username does not already exist."""
    try:
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')

        if not all([username, password, first_name, last_name, email]):
            return JsonResponse({"error": "Missing required fields"})

        username_exist = User.objects.filter(username=username).exists()

        if username_exist:
            return JsonResponse({"userName": username, "error": "Already Registered"})

        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name,
                                        last_name=last_name, password=password, email=email)
        login(request, user)

        return JsonResponse({"userName": username, "status": "Authenticated"})

    except json.JSONDecodeError:
        logger.exception("JSON decode error")
        return JsonResponse({"error": "Invalid JSON data"})
    except Exception as e:
        logger.exception("An error occurred during registration")
        return JsonResponse({"error": str(e)})

# Update the `get_dealerships` render list of dealerships
def get_dealerships(request, state="All"):
    """Fetches dealership data, either all or by specific state."""
    try:
        endpoint = f"/fetchDealers/{state}" if state != "All" else "/fetchDealers"
        dealerships = get_request(endpoint)
        return JsonResponse({"status": 200, "dealers": dealerships})

    except Exception as e:
        logger.exception("An error occurred while fetching dealerships")
        return JsonResponse({"status": 500, "message": str(e)})

def get_dealer_reviews(request, dealer_id):
    """Fetches dealer reviews and analyzes sentiment."""
    try:
        if dealer_id:
            endpoint = f"/fetchReviews/dealer/{dealer_id}"
            reviews = get_request(endpoint)

            for review_detail in reviews:
                response = analyze_review_sentiments(review_detail['review'])
                review_detail['sentiment'] = response.get('sentiment', 'Unknown')

            return JsonResponse({"status": 200, "reviews": reviews})

        return JsonResponse({"status": 400, "message": "Bad Request"})

    except Exception as e:
        logger.exception("An error occurred while fetching reviews")
        return JsonResponse({"status": 500, "message": str(e)})

def get_dealer_details(request, dealer_id):
    """Fetches details of a specific dealer."""
    try:
        if dealer_id:
            endpoint = f"/fetchDealer/{dealer_id}"
            dealership = get_request(endpoint)
            return JsonResponse({"status": 200, "dealer": dealership})

        return JsonResponse({"status": 400, "message": "Bad Request"})

    except Exception as e:
        logger.exception("An error occurred while fetching dealer details")
        return JsonResponse({"status": 500, "message": str(e)})

# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request):
    """Submits a review for a dealer."""
    try:
        if not request.user.is_anonymous:
            data = json.loads(request.body)
            response = post_review(data)
            return JsonResponse({"status": 200})

        return JsonResponse({"status": 403, "message": "Unauthorized"})

    except json.JSONDecodeError:
        logger.exception("JSON decode error")
        return JsonResponse({"status": 400, "message": "Invalid JSON data"})
    except Exception as e:
        logger.exception("An error occurred while posting review")
        return JsonResponse({"status": 500, "message": str(e)})

# Get List of Cars
def get_cars(request):
    """Returns the list of car models."""
    try:
        count = CarMake.objects.count()

        if count == 0:
            initiate()

        car_models = CarModel.objects.select_related('car_make')
        cars = [
            {
                "CarModel": car_model.name,
                "CarMake": car_model.car_make.name
            } for car_model in car_models
        ]

        return JsonResponse({"CarModels": cars})

    except Exception as e:
        logger.exception("An error occurred while fetching cars")
        return JsonResponse({"status": 500, "message": str(e)})
