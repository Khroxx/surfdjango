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
        assert self.corporation.name == "Test Corp"
        assert self.corporation.address == "Test Address 123"
        assert self.corporation.url == "https://testdomain.com"
        assert self.corporation.user == self.user

    def test_user_created(self):
        assert self.user.username == "testuser"

    def test_user_corp_relationship(self):
        assert self.user.corporations.count() == 1
        assert self.user.corporations.first() == self.corporation
