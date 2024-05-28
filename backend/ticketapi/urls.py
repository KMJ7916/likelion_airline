from django.urls import path
from . import views

urlpatterns = [
    path('ticketapi/',views.ticketget),
]