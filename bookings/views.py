from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm
from .models import Booking


# View to display homepage
def home(request):
    return render(request, "bookings/home.html")


# View to display the restaurant menu
def menu(request):
    return render(request, "bookings/menu.html")


# View to allow a new user to sign up for an account
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "bookings/signup.html", {"form": form})


# View to display and handle the booking form
# User must be logged in to create a booking
@login_required
def make_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            # Extract date and time from the form data
            booking_date = form.cleaned_data["booking_date"]
            booking_time = form.cleaned_data["booking_time"]

            # Check if a booking already exists for the selected date and time
            existing_booking = Booking.objects.filter(
                booking_date=booking_date,
                booking_time=booking_time
            ).exists()

            if existing_booking:
                # If a booking already exists, add an error to the form
                form.add_error(
                    None,
                    "Sorry, there is already a booking at this time. Please choose a different time."
                )
            else:
                # Save booking, but attach the logged-in user first
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()

                messages.success(request, "Your booking has been created successfully.")
                return redirect("my_bookings")
    else:
        # If GET request, display a blank booking form
        form = BookingForm()

    # Render the booking form template
    return render(request, "bookings/make_booking.html", {"form": form})


# View to show only the logged-in user's bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("booking_date", "booking_time")
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})


# View to allow a user to edit their own booking
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            booking_date = form.cleaned_data["booking_date"]
            booking_time = form.cleaned_data["booking_time"]

            # Check if another booking already exists for the updated date/time
            existing_booking = Booking.objects.filter(
                booking_date=booking_date,
                booking_time=booking_time
            ).exclude(id=booking.id).exists()

            if existing_booking:
                form.add_error(
                    None,
                    "Sorry, there is already a booking at this time. Please choose a different time."
                )
            else:
                form.save()
                messages.success(request, "Your booking has been updated successfully.")
                return redirect("my_bookings")
    else:
        form = BookingForm(instance=booking)

    return render(request, "bookings/edit_booking.html", {"form": form, "booking": booking})


# View to allow a user to delete their own booking
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been deleted successfully.")
        return redirect("my_bookings")

    return render(request, "bookings/delete_booking.html", {"booking": booking})