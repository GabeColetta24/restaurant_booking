from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm

# View to display homepage
def home(request):
    return HttpResponse("Welcome to the Restaurant Booking System!")


# View to display and handle booking form
def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking if form data is valid
            form.save()
            # Redirect user to the booking success page
            return render(request, 'bookings/booking_success.html')
    else:
        # If GET request, show a blank booking form
        form = BookingForm()
    # Render the booking form template
    return render(request, 'bookings/make_booking.html', {'form': form})
