from django.urls import path
from . import views
from .views import UserDeleteView

urlpatterns = [
    path('signup/',views.signup),
    path('login/',views.login),
    path('delete-account/<int:pk>/', UserDeleteView.as_view(), name='delete-account'),

]