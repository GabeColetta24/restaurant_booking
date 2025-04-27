from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Restaurant Booking System!")


# View to display and handle booking form
def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bookings/booking_success.html')
    else:
        form = BookingForm()
    return render(request, 'bookings/make_booking.html', {'form': form})
