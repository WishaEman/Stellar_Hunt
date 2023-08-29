from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User


class AuthenticationTestCase(APITestCase):
    """ Test case class for testing authentication-related endpoints  """

    def setUp(self):
        """ Create a user for login and logout testing """

        self.user = User.objects.create_user(
            username='Meeral',
            password='123',
            email='meeral@example.com',
            full_name='Meeral User',
            address='456 Second St',
            phone_number='9876543210',
            gender='female'
        )

    def test_user_signup(self):
        """ Test user signup endpoint and verify successful signup response. """

        data = {
            'username': 'testuser',
            'email': 'test@gmail.com',
            'password': 'testpassword',
            'full_name': 'Test User',
            'address': '123 Main St',
            'phone_number': '1234567890',
            'gender': 'male',
        }
        response = self.client.post(reverse('authentication_api:signup'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login(self):
        """ Test user login endpoint and verify successful login response. """

        data = {
            'username': 'Meeral',
            'password': '123',
        }
        response = self.client.post(reverse('authentication_api:login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_user_logout(self):
        """ Test user logout endpoint after logging in and verify successful logout response. """

        user_response = self.client.post(reverse('authentication_api:login'), {
            'username': 'Meeral',
            'password': '123'
        })
        self.assertEqual(user_response.status_code, status.HTTP_200_OK)
        token = user_response.data['token']
        response = self.client.get(reverse('authentication_api:logout'), HTTP_AUTHORIZATION=f"Token {token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
