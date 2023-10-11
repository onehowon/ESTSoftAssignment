
from django.urls import path
from .views import Login, Join, LogOut, UpdateProfile


urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('join', Join.as_view(), name='join'),
]