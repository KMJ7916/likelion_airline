from django.urls import path
from . import views

urlpatterns = [
    path('flightapi/',views.flightget),
]