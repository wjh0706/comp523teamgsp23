from django.test import TestCase

from ..model import User, Project, Scene, Take, Capture

class SceneModelValidationTests(TestCase):

    def sceneTest(self):
        scene = Scene()
        scene.sid = 12345
        scene.scene_name = "test scene"
        self.assertEqual(12345, scene.sid)

