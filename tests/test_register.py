import unittest
from fastapi.testclient import TestClient
import os
import sys


directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(directory)

import main
from tests_responses import get_UID

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(main.app)

    def test_register_user_valid(self):
        # Test valid registration data
        valid_data = {
            "name": "John Doe",
            "email": "john66ny@gmail.com",
            "password": "secretpaSS123",
            "referral_code": "ABC123",
        }
        response = self.client.post("/register/", data=valid_data)
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")
        self.assertEqual(valid_data, response)

    def test_register_user_no_referral(self):
        # Test registration without referral code
        no_referral_data = {
            "name": "Alice Smith",
            "email": "alice@example.com",
            "password": "anoTher1235",
        }
        response = self.client.post("/register/", data=no_referral_data)
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")
        self.assertEqual(response.json(), {"UID": get_UID(), "response": "Success"})

    def test_register_user_invalid_email(self):
        invalid_email_data = {
            "name": "Invalid Email",
            "email": "invalid_email",
            "password": "anoTher1235",
        }
        response = self.client.post("/register/", data=invalid_email_data)
        assert response.status_code == 400, f"Expected 400, but got {response.status_code}"

    def test_register_user_empty_fields(self):
        empty_data = {
            "name": "",
            "email": "empty@example.com",
            "password": "",
        }
        response = self.client.post("/register/", data=empty_data)
        assert response.status_code == 422, f"Expected 400, but got {response.status_code}"

    def test_register_user_duplicate_email(self):
        duplicate_email_data = {
            "name": "Duplicate Email",
            "email": "john@example.com",  # Use an existing email
            "password": "anoTher1235",
        }
        response = self.client.post("/register/", data=duplicate_email_data)
        assert response.status_code == 409, f"Expected 409, but got {response.status_code}"
    
    
if __name__ == "__main__":
    unittest.main()
