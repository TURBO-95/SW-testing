import pytest
import random
import requests
import urllib3
from datetime import datetime

# Disable SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://localhost:7123/api"
TEST_EMAIL = f"test_{datetime.now().timestamp()}@example.com"
TEST_PASSWORD = "TestPassword1234!"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIzMGRhNzFlNi1lOTI1LTQ2NTAtYTA5Zi1mZGY2ZDhkMDFiY2YiLCJyb2xlIjoiYWRtaW5pc3RyYXRvciIsImV4cGlyZXMiOiI1LzIwLzIwMjUgMzo0NjoyMCBBTSIsIm5iZiI6MTc0NzEwNzk4MCwiZXhwIjoxNzQ3NzEyNzgwLCJpYXQiOjE3NDcxMDc5ODB9.lwUbPXYjXiVu_RLBDl5X4v4bMhexQCkSxeEQmeMOvQo"

# Test data
class TestAPI:
    '''Test API endpoints for signup, signin, and change password'''
    
    def test_signup(self):
        """Test signup"""
        
        user_data = {
            "firstName": "Test",
            "lastName": "User",
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD,
            "role": "dentist",
            "gender": "Male"
        }
        response = requests.post(
            f"{BASE_URL}/signup",
            json=user_data,
            verify=False
        )
        
        assert response.status_code == 200
        print("✓ Signup test passed")

    def test_signin(self):
        """Test signin"""
        credentials = {
            "email": "test_1747105223.677129@example.com",
            "password": TEST_PASSWORD
        }
        response = requests.post(
            f"{BASE_URL}/signin",
            json=credentials,
            verify=False
        )
        assert response.status_code == 200
        
        print("✓ Signin test passed")
        
    def test_change_password(self):
        """Test change password"""
        password_data = {
            "password": TEST_PASSWORD,
            "newPassword": "TestPassword1234!"
        }
        response = requests.put(
            f"{BASE_URL}/changepassword",
            json=password_data,
            verify=False,
            headers={'Authorization': f'Bearer {TOKEN}'}
        )
        assert response.status_code == 200
        print("✓ Change password test passed")
        
    def test_patient_details(self):
        """Test patient details"""
        response = requests.get(
            f"{BASE_URL}/userDetails",
            params={"id": 1},
            verify=False,
            headers={'Authorization': f'Bearer {TOKEN}'}
        )
        assert response.status_code == 200
        print("✓ Patient details test passed")
        
        
        
    '''clinic details, add members, add patient, and team members'''
        
    def test_add_members(self):
        """Test ADD-members"""
        credentials = {
            
            "firstName": "Test",
            "lastName": "Member",
            "email": TEST_EMAIL,
            "Phone": "1234567890",
            "role": "dentist",
            "specialization": "dentist",
            
        }
        response = requests.post(
            f"{BASE_URL}/clinic/add-member",
            json = credentials,
            verify=False,
            headers={'Authorization': f'Bearer {TOKEN}'}
        )
        assert response.status_code == 200
        print("✓ Team members test passed")

    def test_team_members(self):
        """Test team-members"""
        response = requests.get(
            f"{BASE_URL}/clinic/team-members",
            verify=False,
            headers={'Authorization': f'Bearer {TOKEN}'}
        )
        assert response.status_code == 200
        print("✓ Team members test passed")
        
    def test_add_patient(self):
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
        assert response.status_code == 200
        print("✓ Team members test passed")    
    
    '''Test Dentist'''
        
    def test_GET_Dentist(self):
        """Test DENTIST"""
        response = requests.get(
            f"{BASE_URL}/Dentist",
            verify=False,
            headers={'Authorization': f'Bearer {TOKEN}'}
        )
        assert response.status_code == 200
        print("✓ Team members test passed")

    
    '''Test Patients'''
    def test_GET_Patients(self):
        """Test GET PATIENTS"""
        response = requests.get(
            f"{BASE_URL}/Clinic/Patients",
            verify=False,
            headers={'Authorization': f'Bearer {TOKEN}'}
        )
        assert response.status_code == 200
        print("✓ Team members test passed")
    
    def test_create_appointment(self):
        """Test create appointment"""
        credentials = {
            "patientId": random.randint(3,50),
            "dentistId": "1",
            "date": "2025-05-13T04:31:36.401Z",
            "startTime": "7:00",
            "endTime": "9:00",
            "treatmentType": "cleaning",
            "notes": "bad breath"
        }
        response = requests.post(
            f"{BASE_URL}/Patients/create-appointment",
            json = credentials,
            verify=False,
            headers={'Authorization': f'Bearer {TOKEN}'}
        )
        assert response.status_code == 200
        print("✓ create appointment test passed")
    

if __name__ == "__main__":
    pytest.main(["-v"])
    # Run the tests