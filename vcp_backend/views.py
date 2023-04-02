from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .model import User, Project, Scene, Take, Capture
from rest_framework import serializers, viewsets, generics
from rest_framework import permissions
from rest_framework.decorators import action
from .serializers import UserSerializer, ProjectSerializer, SceneSerializer, TakeSerializer, CaptureSerializer, \
    UserLoginSerializer, UserLogoutSerializer
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterViewSet(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginViewSet(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class LogoutViewSet(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # permission_classes = [permissions.IsAuthenticated]
    @action(methods=['get'], detail=False, url_path='getprojects', url_name='getProjects')
    def getProjects(self, request):
        user = User.objects.get(token=request.query_params['token'])
        if user:
            projects = Project.objects.all().filter(user=user)
            projectsSer = ProjectSerializer(projects, many=True, context={'request': request})
            return JsonResponse(projectsSer.data, safe=False)
        return JsonResponse([])

    @action(methods=['post'], detail=False, url_path='createproject', url_name='createProject')
    def createProject(self, request):
        user = User.objects.get(token=request.data.get('token'))
        if user:
            new_project = Project(user=user)
            new_project.save()
            serializer = ProjectSerializer(new_project, data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=False, url_path='deleteproject', url_name='deleteProject')
    def deleteProject(self, request):
        user = User.objects.get(token=request.data.get('token', False))
        if user:
            projects = Project.objects.all().filter(user=user)
            project = projects.get(pid=request.data.get("pid"))
            if project:
                try:
                    project.delete()
                except:
                    return JsonResponse({"status": "fail"})
                return JsonResponse({"status": "success"})
            return JsonResponse({"status": "project not found"})
        return JsonResponse({"status": "user not found"})

    @action(methods=['patch'], detail=False, url_path='editproject', url_name='editProject')
    def editProject(self, request):
        user = User.objects.get(token=request.data.get('token'))
        if user:
            projects = Project.objects.all().filter(user=user)
            project = projects.get(pid=request.data.get('pid'))
            if project:
                try:
                    project.project_name = request.data.get('project_name')
                    project.description = request.data.get('description')
                    project.save()
                except:
                    return JsonResponse({"status": "fail"})
                return JsonResponse({"status": "success"})
            return JsonResponse({"status": "project not found"})
        return JsonResponse({"status": "user not found"})


class SceneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer

    # permission_classes = [permissions.IsAuthenticated]

    @action(methods=['get'], detail=False, url_path='getscenes', url_name='getScenes')
    def getScenes(self, request):
        user = User.objects.get(token=request.query_params['token'])
        if user:
            projects = Project.objects.all().filter(user=user)
            project = projects.get(pid=request.query_params['pid'])
            if project:
                scenes = Scene.objects.all().filter(project=project)
                scenesSer = SceneSerializer(scenes, many=True, context={'request': request})
                return JsonResponse(scenesSer.data, safe=False)
        return JsonResponse([])

    @action(methods=['post'], detail=False, url_path='createscene', url_name='createScene')
    def createScene(self, request):
        user = User.objects.get(token=request.data.get('token'))
        if user:
            projects = Project.objects.all().filter(user=user)
            project = projects.get(pid=request.data.get('pid'))
            if project:
                new_scene = Scene(project=project)
                new_scene.save()
                serializer = SceneSerializer(new_scene, data=request.data, context={'request': request})
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return JsonResponse({"status": "fail"})

    @action(methods=['delete'], detail=False, url_path='deletescene', url_name='deleteScene')
    def deleteScene(self, request):
        user = User.objects.get(token=request.data.get('token', False))
        if user:
            scene = Scene.objects.all().get(sid=request.data.get('sid'))
            if scene:
                try:
                    scene.delete()
                except:
                    return JsonResponse({"status": "fail"})
                return JsonResponse({"status": "success"})
            return JsonResponse({"status": "scene not found"})
        return JsonResponse({"status": "user not found"})

    @action(methods=['patch'], detail=False, url_path='editscene', url_name='editScene')
    def editScene(self, request):
        user = User.objects.get(token=request.data.get('token'))
        if user:
            scene = Scene.objects.all().get(sid=request.data.get('sid'))
            if scene:
                try:
                    scene.scene_name = request.data.get('scene_name')
                    scene.description = request.data.get('description')
                    scene.save()
                except:
                    return JsonResponse({"status": "fail"})
                return JsonResponse({"status": "success"})
        return JsonResponse({"status": "fail"})


class TakeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Take.objects.all()
    serializer_class = TakeSerializer

    # permission_classes = [permissions.IsAuthenticated]

    @action(methods=['get'], detail=False, url_path='gettakes', url_name='getTakes')
    def getTakes(self, request):
        user = User.objects.get(token=request.query_params['token'])
        if user:
            scene = Scene.objects.all().get(sid=request.query_params['sid'])
            if scene:
                takes = Take.objects.all().filter(scene=scene)
                takesSer = TakeSerializer(takes, many=True, context={'request': request})
                return JsonResponse(takesSer.data, safe=False)
        return JsonResponse([])

    @action(methods=['post'], detail=False, url_path='createtake', url_name='createTake')
    def createTake(self, request):
        user = User.objects.get(token=request.data.get('token'))
        if user:
            scene = Scene.objects.all().get(sid=request.data.get('sid'))
            if scene:
                new_take = Take(scene=scene)
                new_take.save()
                serializer = TakeSerializer(new_take, data=request.data, context={'request': request})
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return JsonResponse({"status": "fail"})

    @action(methods=['delete'], detail=False, url_path='deletetake', url_name='deleteTake')
    def deleteTake(self, request):
        user = User.objects.get(token=request.data.get('token', False))
        if user:
            take = Take.objects.all().get(tid=request.data.get('tid'))
            if take:
                try:
                    take.delete()
                except:
                    return JsonResponse({"status": "fail"})
                return JsonResponse({"status": "success"})
            return JsonResponse({"status": "take not found"})
        return JsonResponse({"status": "user not found"})

    @action(methods=['patch'], detail=False, url_path='edittake', url_name='editTake')
    def editTake(self, request):
        user = User.objects.get(token=request.data.get('token'))
        if user:
            take = Take.objects.all().get(tid=request.data.get('tid'))
            if take:
                try:
                    take.take_name = request.data.get('take_name')
                    take.description = request.data.get('description')
                    take.save()
                except:
                    return JsonResponse({"status": "fail"})
                return JsonResponse({"status": "success"})
        return JsonResponse({"status": "fail"})


class CaptureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer

    # permission_classes = [permissions.IsAuthenticated]

    @action(methods=['get'], detail=False, url_path='getcaptures', url_name='getCaptures')
    def getCaptures(self, request):
        user = User.objects.get(token=request.query_params['token'])
        if user:
            take = Take.objects.all().get(tid=request.query_params['tid'])
            if take:
                captures = Capture.objects.all().filter(take=take)
                capturesSer = CaptureSerializer(captures, many=True, context={'request': request})
                return JsonResponse(capturesSer.data, safe=False)
        return JsonResponse([])

    @action(methods=['post'], detail=False, url_path='createcapture', url_name='createCapture')
    def createCapture(self, request):
        user = User.objects.get(token=request.data.get('token'))
        if user:
            take = Take.objects.all().get(tid=request.data.get('tid'))
            if take:
                new_capture = Capture(take=take)
                new_capture.save()
                serializer = CaptureSerializer(new_capture, data=request.data, context={'request': request})
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return JsonResponse({"status": "fail"})

    @action(methods=['delete'], detail=False, url_path='deletecapture', url_name='deleteCapture')
    def deleteCapture(self, request):
        user = User.objects.get(token=request.data.get('token', False))
        if user:
            capture = Capture.objects.all().get(cid=request.data.get('cid'))
            if capture:
                try:
                    capture.video_file.delete(save=False)
                    capture.delete()
                except:
                    return JsonResponse({"status": "fail"})
                return JsonResponse({"status": "success", "cid": request.data.get('cid')})
            return JsonResponse({"status": "capture not found"})
        return JsonResponse({"status": "user not found"})

    @action(methods=['patch'], detail=False, url_path='editcapture', url_name='editCapture')
    def editCapture(self, request):
        user = User.objects.get(token=request.data.get('token'))
        if user:
            capture = Capture.objects.all().get(cid=request.data.get('cid'))
            if capture:
                try:
                    capture.video_file = request.data.get('video_file')
                    capture.save()
                except:
                    return JsonResponse({"status": "fail"})
                return JsonResponse({"status": "success"})
        return JsonResponse({"status": "fail"})
