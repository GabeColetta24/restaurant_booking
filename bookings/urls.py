from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path("", views.home, name="home"),

    # Booking page (requires login)
    path("book/", views.make_booking, name="make_booking"),

    # Menu page
    path("menu/", views.menu, name="menu"),

    # User authentication
    path("signup/", views.signup, name="signup"),

    # Booking management (CRUD)
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("edit/<int:booking_id>/", views.edit_booking, name="edit_booking"),
    path("delete/<int:booking_id>/", views.delete_booking, name="delete_booking"),
]