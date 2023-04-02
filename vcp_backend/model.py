from django.db import models
from vcp_backend.storage_backend import PublicMediaStorage


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128, unique=True, db_index=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    Logged_in = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return "User %s: %s; %s" % (self.uid, self.username, self.email)


class Project(models.Model):
    pid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_name = models.CharField(max_length=128, db_index=True, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "Project %s: %s by %s" % (self.pid, self.project_name, self.user)


class Scene(models.Model):
    sid = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    scene_name = models.CharField(max_length=128, db_index=True, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "Scene %s: %s in %s" % (self.sid, self.scene_name, self.project)


class Take(models.Model):
    tid = models.AutoField(primary_key=True)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, null=True)
    take_name = models.CharField(max_length=128, db_index=True, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    model_file = models.FileField(null=True, blank=True)
    audio_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return "Take %s: %s in %s" % (self.tid, self.take_name, self.scene)


class Capture(models.Model):
    cid = models.AutoField(primary_key=True)
    take = models.ForeignKey(Take, on_delete=models.CASCADE, null=True)
    video_file = models.FileField(storage=PublicMediaStorage(), null=True, blank=True)

    def __str__(self):
        return "Capture %s" % self.cid
