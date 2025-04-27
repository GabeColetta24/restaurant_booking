from django.contrib import admin
from .models import Booking

# Customize how bookings are displayed in the admin panel
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'booking_date', 'booking_time', 'number_of_guests')

# Register the Booking model with the admin site
admin.site.register(Booking, BookingAdmin)
