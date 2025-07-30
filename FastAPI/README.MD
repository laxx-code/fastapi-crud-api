#  FastAPI Routing Demo

## Description
This is a basic FastAPI project demonstrating routing, path and query parameters, and Pydantic model usage in POST requests.

## Features
- `GET /` – Root route returning a welcome message
- `GET /about` – Sample nested dictionary data
- `GET /user/{id}` – Displays a user by ID (path parameter)
- `GET /user?limit=5&failed=true` – Returns data using query parameters
- `POST /adduser` – Accepts user details using Pydantic

## Requirements
pip install fastapi uvicorn

# How to Run
uvicorn main:app --reload

Then open:
Swagger Docs: http://127.0.0.1:8000/docs
Root: http://127.0.0.1:8000/

## Note
All data is stored temporarily in memory and will reset when the server stops.
Files:
main.py – All FastAPI logic




