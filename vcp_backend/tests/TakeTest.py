from django.test import TestCase

from ..model import User, Project, Scene, Take, Capture

class TakeModelValidationTests(TestCase):

    def takeTest(self):
        take = Take()
        take.tid = 12345
        self.assertEqual(12345, take.tid)

