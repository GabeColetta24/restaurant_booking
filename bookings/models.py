from django.db import models
from django.contrib.auth.models import User


# Booking model to store restaurant reservations
class Booking(models.Model):
    # Link each booking to a registered Django user
    # This allows users to view, edit, and delete only their own bookings
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    # Customer first name
    first_name = models.CharField(max_length=50)

    # Customer last name
    last_name = models.CharField(max_length=50)

    # Customer email address
    email = models.EmailField()

    # Customer phone number
    phone = models.CharField(max_length=20)

    # Date of the booking
    booking_date = models.DateField()

    # Time of the booking
    booking_time = models.TimeField()

    # Number of guests included in the booking
    number_of_guests = models.PositiveIntegerField()

    # String shown in admin panel and elsewhere
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.booking_date} at {self.booking_time}"