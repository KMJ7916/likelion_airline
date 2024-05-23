from django.urls import path
from . import views
from .views import ObtainToken
from .views import DeleteAccount

urlpatterns = [
    path('signup/',views.signup),
    path('login/',views.login),
    path('get_token/', ObtainToken.as_view(), name='get_token'),
    path('delete_account/<int:user_id>/', DeleteAccount.as_view(), name='delete_account'),
]