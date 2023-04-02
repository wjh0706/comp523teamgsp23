from django.test import TestCase

from ..model import User, Project, Scene, Take, Capture
from ..serializers import UserSerializer

class UserModelValidationTests(TestCase):

    def username(self):
        user = User()
        user.username = "test"
        user.uid = 12345
        user.email = "john@test.com"
        self.assertEqual(12345, user.uid)
        self.serializer = UserSerializer(instance=self.user)

