from django.test import TestCase

from ..model import User, Project, Scene, Take, Capture

class CaptureModelValidationTests(TestCase):

    def captureTest(self):
        capture = Capture()
        capture.cid = 12345
        self.assertEqual(12345, capture.cid)

