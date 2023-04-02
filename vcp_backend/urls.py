"""composeexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import  DefaultRouter
from .views import UserViewSet, ProjectViewSet, TakeViewSet, CaptureViewSet, SceneViewSet, RegisterViewSet, LoginViewSet, LogoutViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'takes', TakeViewSet)
router.register(r'captures', CaptureViewSet)
router.register(r'scenes', SceneViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vcp/', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('register/', RegisterViewSet.as_view(), name="register"),
    path('login/', LoginViewSet.as_view(), name="login"),
    path('logout/', LogoutViewSet.as_view(), name="logout")
]
