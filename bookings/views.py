from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from .models import Booking

# View to display homepage
def home(request):
    return render(request, 'bookings/home.html')


# View to display and handle the booking form
def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Extract date and time from the form data
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']

            # Check if a booking already exists for the selected date and time
            existing_booking = Booking.objects.filter(booking_date=booking_date, booking_time=booking_time).exists()

            if existing_booking:
                # If a booking already exists, add an error to the form
                form.add_error(None, 'Sorry, there is already a booking at this time. Please choose a different time.')
            else:
                # Save the booking if no conflict is found
                form.save()
                # Redirect the user to the booking success page
                return render(request, 'bookings/booking_success.html')
    else:
        # If GET request, display a blank booking form
        form = BookingForm()
    
    # Render the booking form template
    return render(request, 'bookings/make_booking.html', {'form': form})


# View to display the restaurant menu
def menu(request):
    return render(request, 'bookings/menu.html')
