import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url', default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    """Make a GET request to the backend server with optional parameters."""
    params = ""
    if kwargs:
        params = '&'.join(f"{key}={value}" for key, value in kwargs.items())

    request_url = f"{backend_url}{endpoint}?{params}"

    print(f"GET from {request_url}")
    try:
        # Make GET request to the backend URL with parameters
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        # Catch network or HTTP exceptions
        print("Network exception occurred")


def analyze_review_sentiments(text):
    """Analyze review sentiments using sentiment analyzer API."""
    request_url = f"{sentiment_analyzer_url}/analyze/{text}"
    try:
        # Make GET request to sentiment analyzer API
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    """Post a review to the backend."""
    request_url = f"{backend_url}/insert_review"
    try:
        # Make POST request to backend server to insert review
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException:
        # Catch network or HTTP exceptions
        print("Network exception occurred")
