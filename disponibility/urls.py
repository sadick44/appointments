from django.urls import path
from .views import user_login, user_register, home, take_appointment

urlpatterns = [
    path('', home, name="home"),
    path('login', user_login, name="login"),
    path('signup', user_register, name="signup"),
    path('appointment', take_appointment, name="appointment")
]