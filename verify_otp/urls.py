
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', RegisterView, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('verify', views.verify, name='verify'),

]
