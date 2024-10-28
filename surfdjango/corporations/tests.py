from django.contrib.auth.hashers import make_password
from django.test import TestCase

from surfdjango.users.models import User

from .models import Corporation

# Create your tests here.


class CorporationToUserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            password=make_password("testpassword"),
        )
        self.corporation = Corporation.objects.create(
            name="Test Corp",
            address="Test Address 123",
            url="https://testdomain.com",
            user=self.user,
        )

    def test_corp_user_created(self):
        self.assertEqual(self.corporation.name, "Test Corp")  # noqa: PT009
        self.assertEqual(self.corporation.address, "Test Address 123")  # noqa: PT009
        self.assertEqual(self.corporation.url, "https://testdomain.com")  # noqa: PT009
        self.assertEqual(self.corporation.user, self.user)  # noqa: PT009

    def test_user_created(self):
        self.assertEqual(self.user.username, "testuser")  # noqa: PT009

    def test_user_corp_relationship(self):
        self.assertEqual(self.user.corporations.count(), 1)  # noqa: PT009
        self.assertEqual(self.user.corporations.first(), self.corporation)  # noqa: PT009
