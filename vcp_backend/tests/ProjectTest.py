from django.test import TestCase

from ..model import User, Project, Scene, Take, Capture

class ProjectModelValidationTests(TestCase):

    def projectTest(self):
        project = Project()
        project.pid = 12345
        project.project_name = "test project"
        self.assertEqual(12345, project.uid)

