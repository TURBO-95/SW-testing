import random, requests
from datetime import datetime

BASE_URL = "https://localhost:7123/api"
TEST_EMAIL = f"test_{datetime.now().timestamp()}@example.com"
TEST_PASSWORD = "TestPassword1234!"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIzMGRhNzFlNi1lOTI1LTQ2NTAtYTA5Zi1mZGY2ZDhkMDFiY2YiLCJyb2xlIjoiYWRtaW5pc3RyYXRvciIsImV4cGlyZXMiOiI1LzIwLzIwMjUgMzo0NjoyMCBBTSIsIm5iZiI6MTc0NzEwNzk4MCwiZXhwIjoxNzQ3NzEyNzgwLCJpYXQiOjE3NDcxMDc5ODB9.lwUbPXYjXiVu_RLBDl5X4v4bMhexQCkSxeEQmeMOvQo"


def test_add_patient():
        """Test ADD-patient"""
        credentials = {
            "firstName": "test",
            "lastName": "patient",
            "email": f"test_{random.randint(1,10000)}@example.com",
            "phone": "0123456789",
            "dateOfBirth": "2025-05-13T04:19:13.071Z",
            "gender": "male",
            "country": "egypt",
            "city": "mansoura",
            "state": "dakahlia",
            "zipCode": "123456",
            "medicalHistory": "string",
            "allergies": "string"
        }
        response = requests.post(
            f"{BASE_URL}/clinic/add-patient",
            json = credentials,
            verify=False,
            headers={'Authorization': f'Bearer {TOKEN}'}
        )
        
for _ in range(20):        
    test_add_patient();