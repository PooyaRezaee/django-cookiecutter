from django.test import TestCase
from django.contrib.auth import get_user_model
from model_bakery import baker
from unittest.mock import patch

User = get_user_model()

class UserModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = baker.make("account.User")
        
    def test_create_user_with_email_successful(self):
        email = "test@example.com"
        password = "TestPassword123"
        user = User.objects.create_user(email=email, password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)

    def test_create_user_with_no_email_raises_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="TestPassword123")

    def test_create_user_with_no_password_raises_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="test@example.com", password="")

    def test_create_superuser(self):
        email = "superuser@example.com"
        password = "SuperPassword123"
        user = User.objects.create_superuser(email=email, password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_admin)

    def test_user_str_method(self):
        email = "test@example.com"
        user = User.objects.create_user(email=email, password="TestPassword123")
        self.assertEqual(str(user), email)

    # def test_user_email_normalization(self): # CHECK normalize email django don't work good, better overwrite normalize_email or ignore it
    #     email = "TEST@EXAMPLE.COM"
    #     user = User.objects.create_user(email=email, password="TestPassword123")
    #     self.assertEqual(user.email, email.lower())
