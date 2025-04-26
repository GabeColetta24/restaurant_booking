from django.db import models

# Model to store customer booking information
class Booking(models.Model):
    # Customer's first name
    first_name = models.CharField(max_length=50)

    # Customer's last name
    last_name = models.CharField(max_length=50)

    # Customer's email address
    email = models.EmailField()

    # Customer's phone number
    phone = models.CharField(max_length=20)

    # Date of the booking (e.g., 2025-04-29)
    booking_date = models.DateField()

    # Time of the booking (e.g., 7:30 PM)
    booking_time = models.TimeField()

    # Number of people for the booking
    number_of_guests = models.PositiveIntegerField()

    # Display booking details clearly in the admin panel and elsewhere
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.booking_date} at {self.booking_time}"
from django.db import models

# Model to store customer booking information
class Booking(models.Model):
    # Customer's first name
    first_name = models.CharField(max_length=50)

    # Customer's last name
    last_name = models.CharField(max_length=50)

    # Customer's email address
    email = models.EmailField()

    # Customer's phone number
    phone = models.CharField(max_length=20)

    # Date of the booking (e.g., 2025-04-29)
    booking_date = models.DateField()

    # Time of the booking (e.g., 7:30 PM)
    booking_time = models.TimeField()

    # Number of people for the booking
    number_of_guests = models.PositiveIntegerField()

    # Display booking details clearly in the admin panel and elsewhere
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.booking_date} at {self.booking_time}"
