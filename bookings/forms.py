from django import forms
from .models import Booking

# Form for users to create a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'booking_date',
            'booking_time',
            'number_of_guests'
        ]
