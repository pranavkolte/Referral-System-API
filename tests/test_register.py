from fastapi.testclient import TestClient
import os
import sys

# Add the necessary directory to the Python path
directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(directory)

import main
from tests_responses import get_UID

client = TestClient(main.app)

def test_register_user_valid():
    # Test valid registration data
    valid_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "secretpassword",
        "referral_code": "ABC123",
    }
    response = client.post("/register/", data=valid_data)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json() == {"UID": get_UID(), "response": "Success"}

def test_register_user_no_referral():
    # Test registration without referral code
    no_referral_data = {
        "name": "Alice Smith",
        "email": "alice@example.com",
        "password": "anotherpassword",
    }
    response = client.post("/register/", data=no_referral_data)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json() == {"UID": get_UID(), "response": "Success"}

def test_register_user_invalid_email():
    # Test invalid email format
    invalid_email_data = {
        "name": "Invalid Email",
        "email": "invalid_email",
        "password": "secretpassword",
    }
    response = client.post("/register/", data=invalid_email_data)
    assert response.status_code == 400

def test_register_user_empty_fields():
    # Test empty name and password
    empty_data = {
        "name": "",
        "email": "empty@example.com",
        "password": "",
    }
    response = client.post("/register/", data=empty_data)
    assert response.status_code == 400

def test_register_user_duplicate_email():
    # Test duplicate email
    duplicate_email_data = {
        "name": "Duplicate Email",
        "email": "john@example.com",  # Use an existing email
        "password": "secretpassword",
    }
    response = client.post("/register/", data=duplicate_email_data)
    assert response.status_code == 409

# Add more test cases as needed

if __name__ == "__main__":
    test_register_user_valid()
    test_register_user_no_referral()
    test_register_user_invalid_email()
    test_register_user_empty_fields()
    test_register_user_duplicate_email()
