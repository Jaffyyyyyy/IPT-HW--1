from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import User

class UserCreateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_user')

    def test_create_user_success(self):
        payload = {
            "username": "newuser",
            "email": "newuser@example.com"
        }
        response = self.client.post(
            self.url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data['message'], "User created successfully")
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_create_user_missing_fields(self):
        payload = {
            "username": "incompleteuser"
            # Missing email
        }
        response = self.client.post(
            self.url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        response_data = response.json()
        self.assertIn("error", response_data)
        # Check if error message indicates missing fields
        self.assertIn("Missing field", response_data['error'])
