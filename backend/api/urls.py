from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup),
    path('login/',views.login),
    # path('delete-account/<int:pk>/', UserDeleteView.as_view(), name='delete-account'),

]