from django.test import TestCase
from usuario.models import User

class TestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def create_user(self):
        user = User.objects.create(name='test', email='test@test.com', password='1234')
        user.save()
        return user

    def login(self):
        user_logged = self.client.login(name='test', email='test@test.com', password='1234')
        return user_logged