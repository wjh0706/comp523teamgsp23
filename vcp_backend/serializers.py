# from django.contrib.auth.models import User, Group
from uuid import uuid4
from django.db.models import Q
from .model import User, Project, Scene, Take, Capture
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(max_length=32)

    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email']


class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        if not username and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in username:
            user = User.objects.filter(
                Q(email=username) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(email=username)
        else:
            user = User.objects.filter(
                Q(username=username) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(username=username)
        # if user.Logged_in:
        #     raise ValidationError("User already logged in.")
        user.Logged_in = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )


class UserLogoutSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        token = data.get("token", None)
        print(token)
        user = None
        try:
            user = User.objects.get(token=token)
            if not user.Logged_in:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.Logged_in = False
        user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = User
        fields = (
            'token',
            'status',
        )


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'pid', 'user', 'project_name', 'create_time', 'description']


class SceneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scene
        fields = ['url', 'sid', 'project', 'scene_name', 'description']


class TakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Take
        fields = ['url', 'tid', 'scene', 'take_name', 'description', 'model_file', 'audio_file']


class CaptureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Capture
        fields = ['url', 'cid', 'take', 'video_file']
