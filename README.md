# fitness_booking_app
A FastAPI backend to manage fitness class bookings with timezone-aware scheduling (IST-based), SQLite database, slot validation, and client booking retrieval. Includes seed data, input validation, error handling, and basic tests.

## Overview

This project implements a backend API for a fictional fitness studio allowing clients to view fitness classes (Yoga, Zumba, HIIT), book spots, and view their bookings. The API is built using FastAPI, with:

- Class scheduling in IST timezone stored internally
- Dynamic timezone conversions on class listings
- SQLite database with SQLAlchemy ORM (file-based)
- Input validation and error handling with Pydantic
- Modular, readable, and maintainable code structure
- Basic logging and automated tests

---

## Features Implemented

- **GET /classes**: Lists all upcoming classes with timezone-aware datetime
- **POST /book**: Allows booking a class spot with validation and slot management
- **GET /bookings**: Retrieves all bookings by client email

---

## Technology Stack

- Python 3.10+
- FastAPI for API framework
- SQLAlchemy ORM with SQLite database (file)
- Pydantic for request and response validation
- pytest for testing

---

## Setup Instructions

1. Clone or download the repository:

git clone <repository_url>
cd fitness_booking

text

2. Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

text

3. Install dependencies:

pip install -r requirements.txt

text

4. Start the FastAPI server:

uvicorn main:app --reload

text

The API will be accessible at http://127.0.0.1:8000

---

## API Usage Examples

### 1. List Classes

List all upcoming classes, optionally converting times to a timezone (default IST).

curl -X GET "http://127.0.0.1:8000/classes?tz=UTC"

text

### 2. Book a Class Spot

Book a spot by providing class ID and client info.

curl -X POST "http://127.0.0.1:8000/book"
-H "Content-Type: application/json"
-d '{"class_id":1,"client_name":"John Doe","client_email":"john@example.com"}'

text

### 3. View Bookings

Retrieve bookings by client email.

curl -X GET "http://127.0.0.1:8000/bookings?client_email=john@example.com"
