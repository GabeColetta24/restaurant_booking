# Restaurant Booking System

## Overview

The Restaurant Booking System is a full-stack web application designed for customers to book tables online and for restaurant owners to manage bookings easily. 
It features date and time-based reservations, prevents double bookings, and provides a simple menu display. 
The system aims to improve the restaurant's booking efficiency and enhance customer satisfaction.

## Features

- Date and time-based table bookings
- Prevents double bookings for the same time slot
- Booking success confirmation page
- Menu page displaying available dishes
- Admin panel for managing bookings
- Responsive design with custom CSS styling
- User-friendly navigation bar across pages
- Form validation and error handling for bookings

## Technologies Used

- HTML5
- CSS3
- JavaScript (basic form validation and dynamic interactions)
- Python 3
- Django 4
- PostgreSQL (local database)
- Gunicorn (production server)
- dj-database-url (for database connection on Heroku)
- psycopg2-binary (PostgreSQL adapter)
- Git and GitHub (version control)
- Heroku (cloud deployment)

## Installation

Follow these steps to run the project locally:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/GabeColetta24/restaurant_booking.git

2. **Navigate to the project folder**:
   cd restaurant_booking

3. **Create and activate a virtual environment**:
   python3 -m venv venv
   source venv/bin/activate

4. **Install the required dependencies**:
   pip install -r requirements.txt

5. **Configure the database**:
   Ensure PostgreSQL is installed and running locally.
   Create a database named restaurant_booking_db

6. **Apply database migrations**:
   python manage.py migrate

7. **Run the development server**:
   python manage.py runserver

8. **Open the app in your browser**:
   http://127.0.0.1:8000/
   

## How to Use

1. Visit the homepage where you will see a welcome message and navigation links.
2. To make a booking:
   - Click on the **Book a Table** link in the navigation bar.
   - Fill in your details, select a date, time, and number of guests.
   - Submit the booking form.
   - If the booking is successful, you will be shown a success message.
   - If there is already a booking at the chosen time, you will be asked to pick a different time.
3. To view the restaurant menu:
   - Click on the **Menu** link in the navigation bar to see the list of dishes available.
4. Admin users can log in to the Django admin panel to manage bookings.

