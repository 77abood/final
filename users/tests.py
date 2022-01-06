from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .models import *
from users.forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.test import Client


class URLTest(SimpleTestCase):

    def test_about_page(self):
        response = self.client.get('/contact')
        self.assertRedirects(response, '/contact/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_home_page(self):
        url = reverse('Web-Home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/home.html')
        self.assertContains(response, 'COVID-19 Vaccination Variety')

    def test_faq_page(self):
        response = self.client.get('/FAQ')
        self.assertRedirects(response, '/FAQ/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_contact_page(self):
        response = self.client.get('/contact')
        self.assertRedirects(response, '/contact/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)


    def test_user_register_page(self):
        response = self.client.get('/register')
        self.assertRedirects(response, '/register/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register(self):
        """Register Function Functionality"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")

    def test_login(self):
        """Login Functionality Testing"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")

    def test_logout(self):
        """Logout Function Functionality"""
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/logout.html")

    def test_user_register(self):
        """Testing user register pass"""
        self.user = {
            "username": "username",
            "fname": "fname",
            "lname": "lname",
            "email": "email@gmail.com",
            "pass1": "pass1",
            "pass2": "pass1",
        }
        response = self.client.post(reverse("register"), self.user)
        self.assertEqual(response.status_code, 200)

    def test_username_taken(self):
        """Test function to catch username duplications"""
        self.user = {
            "username": "username",
            "fname": "fname",
            "lname": "lname",
            "email": "email@gmail.com",
            "pass1": "pass1",
            "pass2": "pass1",
        }
        self.client.post(reverse("register"), self.user)
        response = self.client.post(reverse("register"), self.user)
        self.assertEqual(response.status_code, 200)

    def test_email_exists(self):
        """Test function to check email duplication"""
        self.user = {
            "username": "username1",
            "fname": "fname",
            "lname": "lname",
            "email": "email@gmail.com",
            "pass1": "pass1",
            "pass2": "pass1",
        }
        self.test_user2 = {
            "username": "username11",
            "fname": "fname",
            "lname": "lname",
            "email": "email@gmail.com",
            "pass1": "pass1",
            "pass2": "pass1",
        }
        self.client.post(reverse("register"), self.user)
        response = self.client.post(reverse("register"), self.test_user2)
        self.assertEqual(response.status_code, 200)

    def test_password_reset_done(self):
        """Testing Password Reset Request"""
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/password_reset.html")

    def test_UserForm_Not_Filled(self):
        data = {
            'username': 'testuser123',
            'email': 'fadybd1@gmail.com',
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())
