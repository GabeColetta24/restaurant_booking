from django import forms
from django.utils import timezone
from .models import Booking


# Form for users to create and update a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "booking_date",
            "booking_time",
            "number_of_guests",
        ]
        widgets = {
            # Use a date picker in the browser
            "booking_date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),

            # Use a time picker in the browser
            "booking_time": forms.TimeInput(attrs={"type": "time"}),
        }

    # Prevent users from making a booking in the past
    def clean_booking_date(self):
        booking_date = self.cleaned_data["booking_date"]

        if booking_date < timezone.localdate():
            raise forms.ValidationError("You cannot make a booking in the past.")

        return booking_date