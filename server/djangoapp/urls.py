from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

APPNAME = 'djangoapp'

urlpatterns = [
    # Path for login
    path('login/', views.login_user, name='login'),

    # Path for logout
    path('logout/', views.logout_user, name='logout'),

    # Path for registration
    path('register/', views.registration, name='register'),
    # Path to get list of cars
    path('get_cars/', views.get_cars, name='get_cars'),

    # Path for dealerships
    path('get_dealers/', views.get_dealerships, name='get_dealers'),

    # Path for getting dealerships by state
    path(
        'get_dealers/<str:state>/',
        views.get_dealerships,
        name='get_dealers_by_state'
    ),

    # Path for dealer details
    path(
        'dealer/<int:dealer_id>/',
        views.get_dealer_details,
        name='dealer_details'
    ),

    # Path for dealer reviews view
    path(
        'reviews/dealer/<int:dealer_id>/',
        views.get_dealer_reviews,
        name='get_dealer_reviews'
    ),

    # Path for adding a review
    path('add_review/', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
