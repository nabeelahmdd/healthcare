from custom.models import User
from django.test import TestCase, Client
from django.urls import reverse
from custom.tests.factories import UserFactory
from rest_framework.test import APIClient
from rest_framework import status
from faker import Faker

fake = Faker()


class UserTestCase(TestCase):
    def test_user_creation(self):
        user = UserFactory()
        self.assertEqual(user.first_name, user.first_name)
        self.assertEqual(user.last_name, user.last_name)
        self.assertEqual(user.email, user.email)
        self.assertEqual(user.phone_number, user.phone_number)
        self.assertEqual(user.category, user.category)


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register-list')
        self.login_url = reverse('login')
        self.user_data = {
            'password': fake.password(),
            'email': fake.email(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'phone_number': "9630856388",
            'category': fake.random_element(elements=('d', 'p', 'r')),
            'is_active': True
        }
        self.user = User.objects.create_user(
            email='testuser@gmail.com', password='Test@123')

    def test_user_registration_valid_data(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_registration_invalid_data(self):
        self.user_data['password'] = '123'
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'email': self.user.email,
            'password': 'Test@123',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'email': fake.email(),
            'password': fake.password(),
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse('token' in response.data)
