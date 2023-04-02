from django.contrib import admin

from .model import User, Project, Scene, Take, Capture

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Scene)
admin.site.register(Take)
admin.site.register(Capture)
