from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView

from .views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenBlacklistView.as_view()),

]