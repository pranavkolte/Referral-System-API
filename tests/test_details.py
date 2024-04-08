import unittest
from fastapi.testclient import TestClient
import os
import sys


directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(directory)

import user_details


class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(user_details.app)

    def test_get_user_details(self):
        valid_data = {
            "id" : "b80549fcb065ae80c8ea3a84a76ac1c418fecffd",
            "name": "Nitesh  Gaikwad",
            "referral_id" : "HEWnBSTq",
            "time" : "2024-04-08 10:58:49.530747",
        }
        response = self.client.get("/get_refer/nitesh342@gmail.com")
        self.assertEqual(response, valid_data)

if __name__ == "__main__":
    unittest.main()