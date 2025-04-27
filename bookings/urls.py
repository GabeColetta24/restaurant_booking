from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # Home page
    path('book/', views.make_booking, name='make_booking'),   # Booking form page
    path('menu/', views.menu, name='menu'),   # Menu page
]
