from django.urls import path
from .views import signUp

urlpatterns = [
    path("register/", view=signUp, name="signup"),
]
