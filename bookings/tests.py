from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Booking


class BookingTests(TestCase):
    """Automated tests for booking functionality and access control."""

    def setUp(self):
        """Create test users and a sample booking."""
        self.user1 = User.objects.create_user(
            username="user1",
            password="testpass123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="testpass123"
        )

        self.future_date = timezone.localdate() + timedelta(days=1)

        self.booking = Booking.objects.create(
            user=self.user1,
            first_name="Gabe",
            last_name="Coletta",
            email="gabe@example.com",
            phone="123456789",
            booking_date=self.future_date,
            booking_time="18:00",
            number_of_guests=2,
        )

    def test_login_required_for_make_booking(self):
        """Users must be logged in to access the booking page."""
        response = self.client.get(reverse("make_booking"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_logged_in_user_can_create_booking(self):
        """A logged-in user can successfully create a booking."""
        self.client.login(username="user1", password="testpass123")

        response = self.client.post(reverse("make_booking"), {
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "phone": "987654321",
            "booking_date": self.future_date + timedelta(days=1),
            "booking_time": "19:00",
            "number_of_guests": 4,
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.filter(user=self.user1).count(), 2)

    def test_user_cannot_edit_another_users_booking(self):
        """A user cannot edit another user's booking."""
        self.client.login(username="user2", password="testpass123")

        response = self.client.get(reverse("edit_booking", args=[self.booking.id]))
        self.assertEqual(response.status_code, 404)

    def test_user_cannot_delete_another_users_booking(self):
        """A user cannot delete another user's booking."""
        self.client.login(username="user2", password="testpass123")

        response = self.client.post(reverse("delete_booking", args=[self.booking.id]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Booking.objects.filter(id=self.booking.id).exists())