from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from model_bakery import baker
from ...services.user import create_user
from ...models import User


class UserServicesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = baker.make("account.User", email="user1@example.com") # set manual email because baker insert email without normalize email
        cls.user2 = baker.make("account.User")

    def test_create_valid_user(self):
        email = "sample@gmail.com"
        password = "NormalPassword123"
        user = create_user(email, password)

        self.assertIsInstance(user, User)
        self.assertEqual(user.email, email)
        self.assertNotEqual(user.password, password)

    def test_create_by_exist_email(self):
        email = self.user1.email
        password = "samplePassword123"

        result = create_user(email, password)
        self.assertIsNone(result)

    def test_create_by_invalid_email(self):
        invalid_emails = [
            "invalid_email",
            "invalid@email",
            "invalidemail@" "@invalid.email",
        ]
        password = "NormalPassword123"

        for email in invalid_emails:
            with self.assertRaises(ValidationError):
                create_user(email, password)

    def test_create_by_invalid_password(self):
        email = "sample@gmail.com"
        invalid_passwords = [
            "short",
            "sh0rt",
            "justletter",
            "1234587469852",
        ]

        for password in invalid_passwords:
            with self.assertRaises(ValidationError):
                create_user(email, password)
