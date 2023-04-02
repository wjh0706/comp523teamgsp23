from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient

from ..model import User, Project, Scene
from ..serializers import UserSerializer, ProjectSerializer, SceneSerializer
from ..views import UserViewSet


class UserModelValidationTests(TestCase):

    def username(self):
        user = User()
        user.username = "test"
        user.uid = 12345
        user.email = "john@test.com"
        self.assertEqual(12345, user.uid)
        self.serializer = UserSerializer(instance=self.user)
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['url', 'user', 'project_name', 'create_time', 'description']))


class ProjectModelValidationTests(TestCase):

    def project(self):
        project = Project()
        project.pid = 12345
        project.project_name = "test project"
        self.assertEqual(12345, project.uid)
        self.serializer = ProjectSerializer(instance=self.project())
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['url', 'username', 'password', 'email']))


class SceneModelValidationTests(TestCase):

    def sceneTest(self):
        scene = Scene()
        scene.sid = 12345
        scene.scene_name = "test scene"
        self.assertEqual(12345, scene.sid)
        self.serializer = SceneSerializer(instance=self.scene)
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['url', 'project', 'scene_name', 'description']))

class ViesetTests(TestCase):

    def test_view_set(self):
        request = APIRequestFactory().get("")
        user_detail = UserViewSet.as_view({'get': 'retrieve'})
        user = User.objects.create(username="bob", email="a@a.com", password=12345)
        response = user_detail(request, pk=user.pk)
        self.assertEqual(response.status_code, 403)

class UrlTests(TestCase):

    def test_urls(self):
        client = RequestsClient()
        response = client.get('http://localhost:8000/users/')
        self.assertEqual(response.status_code, 403)